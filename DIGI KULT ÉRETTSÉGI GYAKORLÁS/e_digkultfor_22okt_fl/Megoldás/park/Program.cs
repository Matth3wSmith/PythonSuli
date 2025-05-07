namespace park
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //1. feladat
            StreamReader olvas = new StreamReader("felajanlas.txt");

            int agyasSzam = int.Parse(olvas.ReadLine());

            List<Felajanlas> ajanlasok = new List<Felajanlas>();
            int sorszam = 1;
            while (!olvas.EndOfStream)
            {
                string[] vag = olvas.ReadLine().Split(" ");

                ajanlasok.Add(new Felajanlas(int.Parse(vag[0]), int.Parse(vag[1]), Convert.ToChar(vag[2]), sorszam, agyasSzam));
                sorszam++;
            }

            olvas.Close();

            //2. feladat
            Console.WriteLine("2. feladat");
            Console.WriteLine("A felajanálások száma: "+ajanlasok.Count());

            Console.WriteLine();
            //3. feladat
            Console.WriteLine("3. feladat");
            
            Console.WriteLine("A bejárat mindkét oldalán ültetők: " + String.Join(" ", ajanlasok.Where(x => x.mindketOldal).Select(x => x.sorszam)));
            Console.WriteLine();
            //4. feladat
            Console.WriteLine("4. feladat");
            Console.Write("Adja meg egy ágyás sorszámát: ");
            int bekertAgyas = int.Parse(Console.ReadLine());

            // a)
            int beultetni = ajanlasok.Where(x => x.kezd <= bekertAgyas && x.veg >= bekertAgyas).Count();
            Console.WriteLine("A felajánlók száma: " + beultetni);

            // b)
            char[] szinek = ajanlasok.Where(x => x.kezd <= bekertAgyas && x.veg >= bekertAgyas).Select(x=>x.szin).Distinct().ToArray();

            if (beultetni != 0)
            {
                Console.WriteLine("A virágágyás színe, ha csak az első ültet: " + szinek[0]);
            }
            else
            {
                Console.WriteLine("Ezt az ágyást nem ültetik be.");
            }

            //c)
            Console.WriteLine("A virágágyás színei: "+ String.Join(" ",szinek));
            Console.WriteLine();

            //5. feladat
            Console.WriteLine("5. feladat");
            List<int> vallalt = new List<int>();

            foreach (var ajanlas in ajanlasok)
            {
                if (!ajanlas.mindketOldal) { 
                    for (int i = ajanlas.kezd; i < ajanlas.veg + 1; i++)
                    {
                        vallalt.Add(i);
                    }
                }
                else
                {
                    for (int i = ajanlas.kezd; i < agyasSzam + 1; i++)
                    {
                        vallalt.Add(1);
                    }
                    for (int i = 1; i < ajanlas.veg+1; i++)
                    {
                        vallalt.Add(i);
                    }
                }
            }
            vallalt.Distinct();

            if (vallalt.Count() == agyasSzam)
            {
                Console.WriteLine("Minden ágyás beültetésére van jelentkező.");
            }
            else
            {
                int osszBeultetes = ajanlasok.Select(x => x.agyasok).Sum();
                if (osszBeultetes >= agyasSzam)
                {
                    Console.WriteLine("Átszervezéssel megoldható a beültetés.");
                }
                else
                {
                    Console.WriteLine("A beültetés nem oldható meg.");
                }
            }

            //6. feladat

            

        }
    }
}
