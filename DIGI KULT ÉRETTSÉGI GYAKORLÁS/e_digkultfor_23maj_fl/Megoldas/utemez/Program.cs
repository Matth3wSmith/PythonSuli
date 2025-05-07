using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace utemez
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //1. feladat
            StreamReader olvas = new StreamReader("taborok.txt");
            List<Tabor> taborok = new List<Tabor>();
            while (!olvas.EndOfStream) {
                string[] vag = olvas.ReadLine().Split("\t");
                taborok.Add(new Tabor(int.Parse(vag[0]), int.Parse(vag[1]), int.Parse(vag[2]), int.Parse(vag[3]), vag[4], vag[5]));
            }

            olvas.Close();

            //2. feladat
            Console.WriteLine("2. feladat");
            Console.WriteLine($"Az adatsorok száma: {taborok.Count}");
            Console.WriteLine($"Az először rögzítettt tábor témája: {taborok[0].tema}");
            Console.WriteLine($"Az utoljára rögzítettt tábor témája: {taborok[taborok.Count-1].tema}");

            //3. feladat
            Console.WriteLine("3. feladat");
            List<Tabor> zenei = taborok.Where(x => x.tema=="zenei").Select(x => x).ToList();
            if (zenei.Count > 0)
            {
                foreach (Tabor tabor in zenei)
                {
                    Console.WriteLine($"Zenei tábor kezdődik {tabor.kezdHo}. hó {tabor.kezdNap}. napján.");
                }
            }
            else
            {
                Console.WriteLine("Nem volt zenei tábor.");
            }

            //4. feladat
            Console.WriteLine("4. feldat");
            int max = taborok.Max(x=>x.nevek.Length);
            List<Tabor> legtobb = taborok.Where(x => x.nevek.Length == max).ToList();
            Console.WriteLine("Legnépszerűbbek:");
            foreach (Tabor tabor in legtobb)
            {
                Console.WriteLine(String.Join(" ",tabor.kezdHo,tabor.kezdNap,tabor.tema));
            }


            //6. feladat
            Console.WriteLine("6. feladat");
            Console.Write("hó: ");
            int KertHo = int.Parse(Console.ReadLine());
            Console.Write("nap: ");
            int KertNap = int.Parse(Console.ReadLine());

            int szunetNapja = sorszam(KertHo,KertNap);
            int mennyi = taborok.Where(x => sorszam(x.kezdHo,x.kezdNap)<=szunetNapja && szunetNapja<=sorszam(x.vegHo,x.vegNap)).Count();
            Console.WriteLine($"Ekkor éppen {mennyi} tábor tart.");


            //7. feladat
            Console.Write("Adja meg egy tanuló betűjelét: ");
            string tanulo = Console.ReadLine();
            List<Tabor> erdeklodik = taborok.Where(x => x.nevek.Contains(tanulo)).ToList();
            StreamWriter ir = new StreamWriter("egytanulo.txt");
            
            erdeklodik.Sort((left,right)=>sorszam(left.kezdHo,left.kezdNap).CompareTo(sorszam(right.kezdHo,right.kezdNap)));

            foreach (Tabor tabor in erdeklodik)
            {
                ir.WriteLine(tabor.datum()+" "+tabor.tema);
            }
            ir.Close();

            for (int i = 1; i < erdeklodik.Count; i++)
            {
                int aktKezd = sorszam(erdeklodik[i].kezdHo, erdeklodik[i].kezdNap);
                int elozoVeg = sorszam(erdeklodik[i-1].vegHo, erdeklodik[i-1].vegNap);

                if (aktKezd < elozoVeg)
                {
                    Console.WriteLine("Nem mehet el mindegyik táborba.");
                    break;
                }
            }
        }
        //5. feladat
        static int sorszam(int ho, int nap)
        {
            int elsoNap = 15;
            Dictionary<int,int> nyar = new Dictionary<int,int>();
            nyar.Add(6,0);
            nyar.Add(7, 30);
            nyar.Add(8, 61);

            return nyar[ho] + nap - elsoNap;

        }
    }
}
