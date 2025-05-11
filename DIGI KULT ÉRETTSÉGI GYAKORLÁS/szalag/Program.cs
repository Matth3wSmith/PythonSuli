using System.Linq;
using System.Security.Cryptography;

namespace szalag
{
    internal class Program
    {
        //Kezdés 11:30 -20 VÉGE: 12:59 ==> 70 => 1 óra 10 perc
        static void Main(string[] args)
        {
            List<Rekesz> rekeszek = new List<Rekesz>();  
            //1. feladat
            StreamReader olvas = new StreamReader("szallit.txt");

            string[] sor = olvas.ReadLine().Split(" ");
            Rekesz.hossz = int.Parse(sor[0]);
            Rekesz.idoegyseg = int.Parse(sor[1]);
            int sorszam = 1;
            while (!olvas.EndOfStream)
            {
                string[] vag = olvas.ReadLine().Split(" ");
                rekeszek.Add(new Rekesz(int.Parse(vag[0]), int.Parse(vag[1]), int.Parse(vag[2]), int.Parse(vag[3]), sorszam));
                sorszam++;
            }
            olvas.Close();

            //2. feladat
            Console.Write("Adja meg, melyik adatsorra kíváncsi! ");
            int bekertSor = int.Parse(Console.ReadLine());
            Console.WriteLine($"Honnan: {rekeszek[bekertSor-1].honnan} Hova: {rekeszek[bekertSor-1].hova}");
            Console.WriteLine();

            //4. feladat
            Console.WriteLine("4. feladat");
            List<int> szallitasok = rekeszek.Select(x => tav(Rekesz.hossz,x.honnan, x.hova)).ToList();
            int maxHossz = szallitasok.Max();
            Console.WriteLine("A legnagyobb távolság: "+maxHossz);
            List<int> maxI = new List<int>();
            for (int i = 0; i < szallitasok.Count; i++) {
                if (szallitasok[i] == maxHossz)
                {
                    maxI.Add(i+1);
                }
            }
            Console.WriteLine("A maximális távolságú szállítások sorszáma: " + String.Join(" ",maxI));
            Console.WriteLine();

            //5. feladat
            Console.WriteLine("5. feladat");
            int rekeszSum = rekeszek.Where(x => x.atment0 ).Select(x => x.tomeg).Sum();
            Console.WriteLine("A kezdőpont előtt elhaladó rekeszek össztömege: "+rekeszSum);
            Console.WriteLine();

            //6. feladat
            Console.WriteLine("6. feladat");
            Console.Write("Adja meg a kívánt időpontot! ");
            int idopont = int.Parse(Console.ReadLine());
            Console.WriteLine("A szálított rekeszek halmaza: " + String.Join(" ", rekeszek.Where(x => x.vegez > idopont && x.kezd < idopont).Select( x => x.sorszam)));

            //7. feladat
            StreamWriter ir = new StreamWriter("tomeg.txt");

            var helyek = rekeszek.GroupBy(x => x.honnan);
            foreach (var group in helyek) {
                ir.WriteLine(group.Key+ " " + group.Sum(x => x.tomeg));
            }
            ir.Close();

        }
        //3. feladat
        static int tav(int szalaghossz, int indulashelye, int erkezeshelye)
        {
            if (indulashelye > erkezeshelye)
            {
                return 200 - indulashelye + erkezeshelye;
            }
            else
            { 
                return erkezeshelye-indulashelye;
            }

        }
    }
}
