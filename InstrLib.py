import visa
import ASCIIcollection as AA

def RMclose():
	visa.ResourceManager().close()

class N6705:
			
	def __init__(self, address):
		self.rm = visa.ResourceManager()
		self.inst = self.rm.open_resource(address)
		self.inst.write_termination = '\n'
		self.inst.clear()
		self.ID=self.inst.query("*IDN?")
		
	def reset(self):
		self.inst.write("*RST")
		return self
		
	# def IDcheck(self):
		# return self.inst.query("*IDN?")
	
	def setVolt(self, volt, chan='1:4'):
		self.inst.write(f"VOLT {volt}, (@{chan})")
		return self
			
	def setCurr(self, curr_mA, chan='1:4'):
		curr_A=float(curr_mA)/1000
		self.inst.write(f"CURR {curr_A}, (@{chan})")
		return self
		
	def readVolt(self, chan='1:4'):
		return self.inst.query(f"MEAS:VOLT? (@{chan})")
		
	def readCurr(self, chan='1:4'):
		return self.inst.query(f"MEAS:CURR? (@{chan})")
		
	def conOut(self, con=1, chan='1:4'):
		self.inst.write(f'OUTPut {con}, (@{chan})')
		return self
	
	def end(self):
		self.inst.close()
		# self.rm.close()

		
class ZNB:
	
	def __init__(self, address):
		self.rm = visa.ResourceManager()
		self.inst = self.rm.open_resource(address)
		self.inst.write_termination = '\n'
		self.inst.clear()
		self.ID=self.inst.query("*IDN?")
	
	def reset(self):
		self.inst.write("*RST")
		return self
	
	# def IDcheck(self):
		# return self.inst.query("*IDN?")

	def savecsv(self, path, chan=1):
		self.inst.write(f"MMEMory:STORe:TRACe:CHAN {chan},'{path}', FORM, LOGP")
		return self
	
	def saves2p(self, path, chan=1):
		self.inst.write(f"MMEM:STORe:TRAC:PORT {chan}, '{path}', LOGP, 1, 2")
		return self
		
	def savepng(self, path):
		self.inst.write("HCOP:DEV:LANG PNG")
		self.inst.write(f"MMEM:NAME '{path}'")
		self.inst.write("HCOP:DEST 'MMEM'")
		self.inst.write("HCOP")
		return self
		
	def makeMark(self, marknum=1, chan=1):
		self.inst.write(f"CALC{chan}:MARK{marknum} ON")
		return self
		
	def delMark(self, marknum=1, chan=1):
		if marknum==0:
			self.inst.write(f"CALC{chan}:MARK:AOFF")
		else:
			self.inst.write(f"CALC{chan}:MARK{marknum} OFF")
		return self
		
	def moveMark(self, marknum, freq, chan=1):
		self.inst.write(f"CALC{chan}:MARK{marknum}:X {freq}GHz")
		return self
	
	def selTrc(self, trc, chan=1):
		if type(trc)==int:
			trcname=='Trc'+str(trc)
		else:
			trcname=trc
		self.inst.write(f"CALC{chan}:PAR:SEL '{trcname}'")
		return self
	
	def readMark(self, marknum=1, axis='Y', chan=1):
		return self.inst.query(f"CALC{chan}:MARK{marknum}:{axis}?")
	
	def end(self):
		self.inst.close()
		# self.rm.close()
		
class N5183:
	
	def __init__(self, address):
		self.rm = visa.ResourceManager()
		self.inst = self.rm.open_resource(address)
		self.inst.write_termination = '\n'
		self.inst.clear()
		self.ID=self.inst.query("*IDN?")
	
	def reset(self):
		self.inst.write("*RST")
		return self
	
	# def IDcheck(self):
		# return self.inst.query("*IDN?")
			
	def setPower(self, power):
		self.inst.write(f'POW {power}dBm')
		return self
		
	def setFreq(self, freq):
		self.inst.write(f'FREQ:FIX {freq}GHz')
		return self
		
	def conOut(self, con=1):
		if int(con)==1:
			self.inst.write('OUTP ON')
		elif int(con)==0:
			self.inst.write('OUTP OFF')
		else:
			pass
		return self
	
	def end(self):
		self.inst.close()
		# self.rm.close()

class N9030:
	
	def __init__(self, address):
		self.rm = visa.ResourceManager()
		self.inst = self.rm.open_resource(address)
		self.inst.write_termination = '\n'
		self.inst.clear()
		self.ID=self.inst.query("*IDN?")
		
	def reset(self):
		self.inst.write("*RST")
		return self
	
	# def IDcheck(self):
		# return self.inst.query("*IDN?")
		
	def makeMark(self, marknum=1):
		self.inst.write(f'CALC:MARK{marknum}:STAT ON')
		return self
		
	def delMark(self, marknum=1):
		if marknum==0:
			self.inst.write("CALC:MARK:AOFF")
		else:
			self.inst.write(f'CALC:MARK{marknum}:STAT OFF')
		return self
		
	def moveMark(self, marknum, freq):
		self.inst.write(f"CALC:MARK{marknum}:X {freq}GHz")
		return self
		
	def readMark(self, marknum=1, axis='Y'):
		return self.inst.query(f"CALC:MARK{marknum}:{axis.upper()}?")
		
	def peaksearchMark(self, marknum=1):
		self.inst.write(f"CALC:MARK{marknum}:MAX")
		return self
		
	def end(self):
		self.inst.close()
		# self.rm.close()
