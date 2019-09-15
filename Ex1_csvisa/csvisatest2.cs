using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Ivi.Visa.Interop;

namespace csvisatest2
{
    class Program
    {
        static void Main(string[] args)
        {
            ResourceManager rm = new ResourceManager();
            FormattedIO488 inst = new FormattedIO488();

            inst.IO = rm.Open("TCPIP::192.168.0.11::INSTR") as IMessage;

            inst.WriteString("*IDN?");
            String str = inst.ReadString();

            Console.WriteLine(str);

            inst.IO.Close();
            Console.ReadLine();
        }
    }
}
