using System;
using System.Runtime.InteropServices;
using System.Threading;
namespace FiXOR
{
    class Program
    {
        public static string[] TargetList,Banfiles,sucessed,notsucessed;
        public static string Passowrd, Rootprocess, statuspass, timeprocess,optionx;
        public static Byte decryptdata, encryptdata;
        public static int lensuc, X_integrity, posbyte, N_integrity, n;

        static void Intro()

        {
            Console.Clear();
            Console.WriteLine(@"______  ___    ______  _____        🌍: www.icodexys.com");
            Console.WriteLine(@"|  ____(_)  \ / / __ \|  __ \       📧: iCodexys@gmail.com");
            Console.WriteLine(@"| |__   _  \ V / |  | | |__) |      🔨: Jheff Alberty");
            Console.WriteLine(@"|  __| | |  > <| |  | |  _  /       📊: 2.11(07 / 18 / 2021)");
            Console.WriteLine(@"| |    | | / . \ |__| | | \ \ ");
            Console.WriteLine(@"|_|    |_ /_/ \_\____/|_|  \_\      GNU General Public License v3.0");
        }
        static void warning()
        { ConsoleKey kp;
            Console.WriteLine("##      ##    ###    ########  ##    ## #### ##    ##  ######");
            Console.WriteLine("##  ##  ##   ## ##   ##     ## ###   ##  ##  ###   ## ##    ##");  
            Console.WriteLine("##  ##  ##  ##   ##  ##     ## ####  ##  ##  ####  ## ## ");       
            Console.WriteLine("##  ##  ## ##     ## ########  ## ## ##  ##  ## ## ## ##   #### ");
            Console.WriteLine("##  ##  ## ######### ##   ##   ##  ####  ##  ##  #### ##    ##  ");
            Console.WriteLine("##  ##  ## ##     ## ##    ##  ##   ###  ##  ##   ### ##    ## "); 
            Console.WriteLine(" ###  ###  ##     ## ##     ## ##    ## #### ##    ##  ######  ");
            Console.WriteLine(new string('-', 80)+ "|");
            Console.WriteLine("\n|☢️| Please follow the rules & consequences of this action:");
            Console.WriteLine("*--->Forgetting your password means that you will lose your encrypted data forever.... ");
            Console.WriteLine("*--->Any Password that you type or generate, make sure to write it down...Press [P] to show it.");
            Console.WriteLine("*--->Any action encrypt/decrypt a file, will generate a file log 'encryption.log' / 'decryption.log'....");
            Console.WriteLine("*--->FiXOR is capable to detect if a file is encrypted or not...");
            Console.WriteLine("*--->Also is capable to check if the password is correct or not before touch the file.");
            Console.WriteLine("*--->By Pressing [ENTER] you are aware of your own responsibility of your data!");
            Console.WriteLine(new string('-', 80)+ "|\n");
            Console.WriteLine("Press [ENTER] to Proceed or [ESC] to Cancel the process...");
            while (true)
            {
                kp = Console.ReadKey().Key;
                if (kp== ConsoleKey.Enter)
                {
                    break;
                }
                if (kp == ConsoleKey.Escape)
                {
                    Console.WriteLine("Exit....");
                    Environment.Exit(0);
                }
                if (kp == ConsoleKey.P)
                {
                    Console.WriteLine("Your Password: ");
                }


            }
        }
        static void Helpscr()
        {
            Console.WriteLine("\n|File Encryptor tools.\n");
            Console.WriteLine(@"USAGE: Fixor OPTION TARGET | PASSWORD");
            Console.WriteLine(@"TARGET---> Path\Filename\*.*");
            Console.WriteLine(@"OPTION---> -e to encrypt, -d to decrypt and -s to scan encrypted files");
            Console.WriteLine("PASSWORD---> -p specify a QUICK password to encrypt/decrypt [OPTIONAL]\n");
            Console.WriteLine(@"Example:");
            Console.WriteLine(@"fixor -e mydiary.txt");
            Console.WriteLine(@"fixor -d c:\my downloads\handrew.jpg");
            Console.WriteLine(@"fixor -e *.exe");
            Console.WriteLine(@"fixor -d  *.* -p G0dl!k334#");
            Thread.Sleep(5000);
            Console.WriteLine("Exit....");
            Environment.Exit(0);
        }

        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.Unicode;
            /* warning();*/
             
            if (args.Length <=1)
            {
                Intro();
                Helpscr();
            }
            //TargetList=
            /*if (TargetList.Length == 0)
            {
                Intro();
                Helpscr();
            }*/
            if (args.Length == 4)
            {
                if (args[2] == "-p") { Passowrd = args[3]; }
            }

            optionx = args[0];

            if (optionx == "-s")
            {
                Intro();
                Console.WriteLine("\n║ENCRYPTED FILES DETAILS╠" + new string('═', 80) + "╣\n");
            }
            if (optionx == "-e")
            {
                Intro();
                Console.WriteLine("\n║TARGET'S LIST╠" + new string('═', 80) + "╣\n");
            }
            if (optionx == "-d")
            {
                Intro();
                Console.WriteLine("\n║TARGET'S LIST╠" + new string('═', 80) + "╣\n");
            }






        }
    }
}
