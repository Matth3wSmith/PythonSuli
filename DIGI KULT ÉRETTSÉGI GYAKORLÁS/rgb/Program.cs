using System.ComponentModel.DataAnnotations;

namespace rgb
{
    internal class Program
    {

        static List<List<List<int>>> keppontok = new List<List<List<int>>>();
        static void Main(string[] args)
        {
            //1. feladat

            StreamReader olvas = new StreamReader("kep-1.txt");

            while (!olvas.EndOfStream)
            {
                string[] sor = olvas.ReadLine().Split(" ");
                List<List<int>> tempsor = new List<List<int>>();
                for (int i = 0; i < 640*3; i+=3)
                {
                    tempsor.Add (new List<int> { int.Parse(sor[i]), int.Parse(sor[i + 1]), int.Parse(sor[i + 2]) });
                    
                }
                keppontok.Add(tempsor);
            }

            olvas.Close();

            //2. feladat
            Console.WriteLine("2. feladat:");
            Console.WriteLine("Kérem egy képpont adatait!");
            Console.Write("Sor: ");
            int kertSor = int.Parse(Console.ReadLine());
            Console.Write("Oszlop: ");
            int kertOszlop = int.Parse(Console.ReadLine());

            Console.WriteLine($"A képpont színe RGB({String.Join(",",keppontok[kertSor-1][kertOszlop-1])})");

            //3. feladat
            Console.WriteLine("3. feladat:");
            Console.WriteLine("A világos képpontok száma: "+keppontok.Select(x => x.Where(y => y.Sum() > 600).Count()).Sum());

            //4. feladat
            Console.WriteLine("4. feladat:");
            int darkestSum = keppontok.Select(x => x.Select(y => y.Sum()).Min()).Min();
            Console.WriteLine("A legsötétebb pont RGB összege: "+darkestSum);
            List<List<string>> darkest = keppontok.Select(x => x.Where(y => y.Sum()==darkestSum).Select( y => String.Join(",",y)).ToList()).ToList();
            foreach (var item in darkest)
            {
                foreach (var item2 in item)
                {

                    Console.WriteLine($"RGB({item2})");
                }
            }
            //6. feladat
            Console.WriteLine("6. feladat:");
            int utolso = 0;
            int elso = -1;
            for(int i = 0; i < 360; i++)
            {
                bool hatarBool = hatar(i, 10);
                if (hatarBool && elso==-1)
                {
                    elso = i;
                }
                else if (hatarBool)
                {
                    utolso = i;
                }
            }

            Console.WriteLine("A felhő legelső sora: " + (elso+1));
            Console.WriteLine("A felhő legalsó sora: " + (utolso+1));
            /*List<List<List<int>>> hatarok = keppontok.Where((x, i) => hatar(i, 10)).Select(x=>x.ToList()).ToList();
            
            Console.WriteLine("A felhő legelső sora: " + keppontok.FindIndex());*/

        }

        //5. feladat
        static bool hatar(int sorszam, int elteres)
        {
            for(int i = 1; i < 640; i++)
            {
                if (Math.Abs(keppontok[sorszam][i - 1][2] - keppontok[sorszam][i][2]) > elteres)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
