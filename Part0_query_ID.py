import visa
rm = visa.ResourceManager()

hoge = rm.open_resource("GPIB::29::INSTR")

hoge.write_termination = "\n"
hoge.clear()

hoge.write("*IDN?")
print(hoge.read())

print(hoge.query("*IDN?"))

hoge.write("*RST")
hoge.write("OUTP 1, (@1)")

for i in range(1, 11):
    volt = 0.1*i
    time.sleep(0.1)
    hoge.write(f"VOLT {volt}, (@1)")
    print(hoge.query("MEAS:CURR? (@1)"))

hoge.write("OUTP 0, (@1)")
