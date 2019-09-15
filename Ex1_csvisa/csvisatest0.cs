using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace csvisatest0
{
    class Program
    {
        static void Main(string[] args)
        {
            var session = (Ivi.Visa.IMessageBasedSession)
                Ivi.Visa.GlobalResourceManager.Open("TCPIP::192.168.0.11::INSTR");

            session.FormattedIO.WriteLine("*IDN?");
            string idName = session.FormattedIO.ReadLine();

            Console.WriteLine(idName);

            session.Dispose();
            Console.ReadLine();
        }
    }
}
