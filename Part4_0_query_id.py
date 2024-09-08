# import visa  # visa利用を宣言
import pyvisa as visa  # pyvisaの仕様変更

# ResourceManagerを「rm」として生成
rm = visa.ResourceManager()

# VISAアドレスは実際の環境に合わせて変更すること
instr = rm.open_resource("GPIB0::29::INSTR")  # 測定器と通信開始
instr.write_termination = "\n"  # 終端文字に改行を設定する
instr.clear()  # 通信バッファを消去

print(instr.query("*IDN?"))  # 測定器のIDを問い合わせて表示
