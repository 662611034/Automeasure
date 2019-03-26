// add reference-COM-VISA COM 3.0 TypeLibrary
// only nakami

{
	Lvi.Visa.Interop.ResourceManager RM;
	Ivi.Visa.Interop.FormattedIO488 DMM;

	RM = new Ivi.Visa.Interop.ResourceManager();
	DMM = new Ivi.Visa.Interop.FormattedIO488();

	DMM.IO = (Ivi.Visa.Interop.IMessage)RM.Open("GPIB::0::INSTR");
	DMM.WriteString("*IND?");
	// textBox1.Text = DMM.ReadString();
	ID = DMM.ReadString();
	Console.WriteLine("{0}", ID);
	DMM.IO.Close();

	System.Runtime.InteropServices.Marshal.ReleaseComObject(DIMM);
	System.Runtime.InteropServices.Marshal.ReleaseComObject(RM);
}