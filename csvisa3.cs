// add ref-COM-VISA COM 3.0 Type Library
// add "using Ivi.Visa.Interop
// only nakami

ResourceManager rm = new ResourceManaer();
FormattedIO488 inst = new FormattedIO488();

inst.IO = rm.Open("GPIB::0::INSTR") as IMessage;

inst.WriteString("*IDN?");
String str = inst.ReadString();

// MessageBox.Show(str);
Console.WriteLine("*IDN? = {0}", str);

inst.IO.Close();