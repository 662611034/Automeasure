import visa

# 全ての測定器で共通する機能をInstrumentクラスで定義
class Instrument():

    # rmはコードで一つしか存在できないためクラス変数で定義
    rm = visa.ResourceManager()

    # visaアドレスを引数に、通信開始、終端文字設定、バッファクリアを行う
    # ついでにIDを問い合わせてインスタンス変数idに格納
    def __init__(self, address):
        self.instr = Instrument.rm.open_resource(address)
        self.instr.write_termination = "\n"
        self.instr.clear()
        self.id = self.instr.query("*IDN?")

    # 通信終了コマンド
    def close(self):
        self.instr.close()
        return self

    # リセットコマンド
    def reset(self):
        self.instr.write("*RST")
        return self

# Instrumentを継承しN6705(DC電源)クラスを定義
class N6705(Instrument):
            
    # 電圧設定コマンド
    def set_volt(self, volt, chan="1:4"):
        self.instr.write(f"VOLT {volt}, (@{chan})")
        return self

    # 電流設定コマンド、ただし引数はmA単位で取る        
    def set_curr(self, curr_mA, chan="1:4"):
        curr_A = curr_mA/1000
        self.instr.write(f"CURR {curr_A}, (@{chan})")
        return self
        
    # 電圧を取得し実数に変換して返す
    # 複数チャンネル指定は用いない前提
    # 複数チャンネルで取得したい場合はfor文などで対応
    def read_volt(self, chan):
        volt = self.instr.query(f"MEAS:VOLT? (@{chan})")
        return float(volt)
        
    # 電流を取得しmA単位の実数に変換して返す
    def read_curr(self, chan):
        curr = self.instr.query(f"MEAS:CURR? (@{chan})")
        return 1000*float(curr)
        
    # 出力のon/offコマンド
    def onoff_out(self, con=1, chan="1:4"):
        self.instr.write(f"OUTP {con}, (@{chan})")
        return self

# ZNB(ネットワークアナライザ)のクラス
class ZNB(Instrument):

    # マイドキュメントのパス
    path_mydoc = r"C:\Users\Instrument\\Documents"
    
    # 画面上の全てのトレースを.csv形式で保存
    def save_csv(self, path, chan=1):
        self.instr.write(f"MMEM:STOR:TRAC:CHAN {chan},'{path}', FORM, LOGP")
        return self
    
    # 2ポートs-paraデータを保存
    def save_s2p(self, path, chan=1):
        self.instr.write(f"MMEM:STOR:TRAC:PORT {chan}, '{path}', LOGP, 1, 2")
        return self
        
    # 現在画面を.pngでキャプチャ
    def save_png(self, path):
        self.instr.write("HCOP:DEV:LANG PNG")
        self.instr.write(f"MMEM:NAME '{path}'")
        self.instr.write("HCOP:DEST 'MMEM'")
        self.instr.write("HCOP")
        return self
        
    # マーカ生成
    def make_mark(self, marknum=1, chan=1):
        self.instr.write(f"CALC{chan}:MARK{marknum} ON")
        return self
        
    # マーカ削除
    # マーカ番号は0は存在しないことを利用し、番号0の場合全削除
    def del_mark(self, marknum=1, chan=1):
        if marknum==0:
            self.instr.write(f"CALC{chan}:MARK:AOFF")
        else:
            self.instr.write(f"CALC{chan}:MARK{marknum} OFF")
        return self
        
    # マーカ移動
    def move_mark(self, marknum, freq, chan=1):
        self.instr.write(f"CALC{chan}:MARK{marknum}:X {freq}GHz")
        return self
    
    # マーカの値取得
    def read_mark(self, marknum=1, axis="Y", chan=1):
        return self.instr.query(f"CALC{chan}:MARK{marknum}:{axis}?")

    # マーカの値を取得するトレースを選択
    # トレース名は名称指定だが、引数が整数の場合該当番号のトレース選択
    def select_trace(self, trc, chan=1):
        if type(trc)==int:
            trc = f"Trc{trc}"
        else:
            pass
        self.instr.write(f"CALC{chan}:PAR:SEL '{trc}'")
        return self
    
    # sweep typeをCWに、sweep controlをsingleに設定
    # うｐ主がZNBを信号源として使う場合よく使う設定
    def set_mode_CW(self, con=1):
        if con==1:
            self.instr.write("SWE:TYPE CW")
            self.instr.write("INIT:CONT:ALL OFF")
        elif con==0:
            self.instr.write("INIT:CONT:ALL ON")
            self.instr.write("SWE:TYPE LOG")
        else:
            pass
        return self

    # CWモードの信号源周波数設定コマンド
    def set_freq_CW(self, freq):
        self.instr.write(f"FREQ:CW {freq}ghz")
        return self
    
    # CWモードの信号源電力設定コマンド
    def set_power_CW(self, power):
        self.instr.write(f"SOUR:POW {power}dbm")
        return self
        
    # CWモードの信号源周波数取得コマンド
    def read_freq_CW(self):
        return self.instr.query("FREQ:CW?")
    
    # CWモードの信号源電力取得コマンド
    def read_power_CW(self):
        return self.instr.query("SOUR:POW?")
    

# N5183(シグナルジェネレータ)のクラス
class N5183(Instrument):
    
    # 出力電力設定コマンド
    def set_power(self, power):
        self.instr.write(f"POW {power}dBm")
        return self
        
    # 出力周波数設定コマンド
    def set_freq(self, freq):
        self.instr.write(f"FREQ:FIX {freq}GHz")
        return self

    # 出力電力取得コマンド
    def read_power(self):
        return self.instr.query("POW?")

    # 出力周波数取得コマンド
    def read_freq(self):
        return self.instr.query("FREQ:FIX?")
        
    # 出力オンオフ制御コマンド
    def onoff_con(self, con=1):
        if int(con)==1:
            self.instr.write("OUTP ON")
        elif int(con)==0:
            self.instr.write("OUTP OFF")
        else:
            pass
        return self

# N9030(シグナルアナライザ)クラス
class N9030(Instrument):
    
    # マーカ生成コマンド
    def make_mark(self, marknum=1):
        self.instr.write(f"CALC:MARK{marknum}:STAT ON")
        return self
        
    # マーカ削除コマンド
    def del_mark(self, marknum=1):
        if marknum==0:
            self.instr.write("CALC:MARK:AOFF")
        else:
            self.instr.write(f"CALC:MARK{marknum}:STAT OFF")
        return self
        
    # マーカ移動コマンド
    def move_mark(self, marknum, freq):
        self.instr.write(f"CALC:MARK{marknum}:X {freq}GHz")
        return self
        
    # マーカの値取得コマンド
    def read_mark(self, marknum=1, axis="Y"):
        return self.instr.query(f"CALC:MARK{marknum}:{axis}?")
        
    # マーカのpeak searchコマンド
    def peak_search_mark(self, marknum=1):
        self.instr.write(f"CALC:MARK{marknum}:MAX")
        return self
        
    # 画面キャプチャコマンド
    def save_png(self, filepath):
        self.instr.write(f'MMEM:STOR:SCR "{filepath}"')

