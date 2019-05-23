import visa  # おまじないです
import time  # 待機時間を作るために必要な部分です
rm = visa.ResourceManager()  # おまじないです

# GPIBでつながったアドレス29の測定器を呼び出します
hoge = rm.open_resource("GPIB::29::INSTR")

# 以下2行もおまじないです
hoge.write_termination = "\n"
hoge.clear()

hoge.write("*IDN?")  # 機器IDを問い合わせます
print(hoge.read())  # 得られた応答を表示します

print(hoge.query("*IDN?"))  # 問い合わせ、読み取り、表示を1行で済ませます

# 以下で用いるコマンドはN6705専用のものがあります
hoge.write("*RST")  # 機器をリセットします

hoge.write("OUTP 1, (@1)")  # Ch.1の出力をONにします

for i in range(1, 11):  # iを1から10までループさせます
    volt = 0.1*i  # よって電圧は0.1~1Vまでの値を取ります
    hoge.write(f"VOLT {volt}, (@1)")  # Ch.1の電圧を<volt>Vにします
    time.sleep(0.1)  # 電圧を変えたら0.1秒待機します
    print(hoge.query("MEAS:CURR? (@1)"))  # Ch.1の電流を表示します

hoge.write("OUTP 0, (@1)")  # Ch.1の出力をOFFにします