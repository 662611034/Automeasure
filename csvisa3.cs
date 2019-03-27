// add ref-COM-VISA COM 3.0 Type Library
// add "using Ivi.Visa.Interop

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Ivi.Visa.Interop;

namespace csvisa3
{
    class Program
    {
        static void Main(string[] args)
        {
            ResourceManager rm = new ResourceManager();
            FormattedIO488 inst = new FormattedIO488();

            inst.IO = rm.Open("GPIB2::0::INSTR") as IMessage;

            inst.WriteString("*IDN?");
            String str = inst.ReadString();

            // MessageBox.Show(str);
            Console.WriteLine("*IDN? = {0}", str);

            inst.IO.Close();
            Console.ReadLine();
        }
    }
}
