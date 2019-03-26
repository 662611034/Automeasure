// add ref-framework-extension-Ivi.Visa Assembly
// @ solution explorer, Ivi.Visa is added

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
	class Program
	{
		static void Main(string[] args)
		{
			var session = (Ivi.Visa.IMessageBasedSession)
				Ivi.Visa.GlobalResourceManager.Open("GPIB0:0::INSTR");
			
			session.FormattedIO.WriteLine("*IDN?");
			string idName = session.FormattedIO.ReadLine();
			
			Console.WriteLine("*IDN? = {0}", idName);

			session.Dispose();
			session = null;

			Console.WriteLine("Press Enter key to end");
			Console.ReadLine();
		}
	}
}