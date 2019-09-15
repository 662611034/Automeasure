using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace csvisatest1
{
    class Program
    {
        static void Main(string[] args)
        {
            Ivi.Visa.Interop.ResourceManager RM;
            Ivi.Visa.Interop.FormattedIO488 DMM;

            RM = new Ivi.Visa.Interop.ResourceManager();
            DMM = new Ivi.Visa.Interop.FormattedIO488();

            DMM.IO = (Ivi.Visa.Interop.IMessage)RM.Open("TCPIP::192.168.0.11::INSTR");
            DMM.WriteString("*IDN?");
            String ID = DMM.ReadString();
            Console.WriteLine("{0}", ID);
            DMM.IO.Close();

            Console.ReadLine();

            System.Runtime.InteropServices.Marshal.ReleaseComObject(DMM);
            System.Runtime.InteropServices.Marshal.ReleaseComObject(RM);
        }
    }
}
