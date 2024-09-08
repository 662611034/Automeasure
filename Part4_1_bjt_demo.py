# 8行までの文法はID確認のプログラムと同様
# import visa
import pyvisa as visa  # pyvisaの仕様変更

rm = visa.ResourceManager()

dc_dengen = rm.open_resource("TCPIP::192.168.0.11::INSTR")
dc_dengen.write_termination = "\n"
dc_dengen.clear()

dc_dengen.write("*RST")  # 測定器リセットのコマンド送信

dc_dengen.write("CURR 0.6, (@1:3)")  # Ch.1~3の電流上限を0.6Aに設定
dc_dengen.write("OUTP 1, (@1:3)")  # Ch.1~3の出力をONにする
dc_dengen.write("VOLT 1, (@3)")  # Ch.3の電圧を1Vにする
# マイナスの電圧の出力ができないためエミッタの電圧を1Vにしている

# 測定結果の文字列の1行目を生成
result = "vce;vbe=-0.7;vbe=-0.8;vbe=-0.9;vbe=-1\n"

for i in range(11):  # i=0~10でループ
    vce = - 0.1*i  # vce = 0 ~ -1.0
    dc_dengen.write(f"VOLT {1+vce}, (@1)")  # Ch.1の電圧=コレクタ電圧を1+vceにする
    result += str(vce)  # 測定結果の新しい行の最初に現在のvceを書き込む
    for j in range(7, 11):  # j=7~10でループ
        vbe = -0.1 * j  # vbe= -0.7 ~ -1.0
        dc_dengen.write(f"VOLT {1+vbe}, (@2)")  # Ch.2の電圧=ベース電圧を1+vbeにする
        
        # Ch.1を流れる電流を取得し「current」に格納
        # 測定器の応答は文字列であり、最後に改行が付くため「strip」でその改行を取り除く
        current = dc_dengen.query("MEAS:CURR? (@1)").strip()
        
        result += ";" + current  # 読み取った電流値を「；」で区切りながら測定結果に加える
    result += "\n"  # 測定結果を改行する
dc_dengen.write("OUTP 0, (@1:3)")  # 測定が終わったため電源出力をすべてOFFにする

print(result)  # 確認のため結果を画面に表示する

# 測定結果の文字列を「out.txt」に書き出す
with open("out.txt", "w") as f:
    f.write(result)

dc_dengen.close()  # 電源との通信を終了する
rm.close()  # ResourceManagerを閉じる
#  プログラムが終了すれば自動でcloseされるため簡単なプログラムでは付けなくても良い
