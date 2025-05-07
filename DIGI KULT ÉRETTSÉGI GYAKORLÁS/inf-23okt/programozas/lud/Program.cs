namespace lud
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //1 .feladat
            //Ösvények beolvasása
            List<string> osvenyek = new List<string>();
            StreamReader olvas = new StreamReader("osvenyek.txt");
            while (!olvas.EndOfStream)
            {
                osvenyek.Add(olvas.ReadLine());
            }
            olvas.Close();
            //Dobások beolvasás
            olvas = new StreamReader("dobasok.txt");
            string[] sor = olvas.ReadLine().Split(" ");
            List<int> dobasok = sor.Select(x => int.Parse(x)).ToList();
            olvas.Close();

            //2. feladat
            Console.WriteLine("2. feladat");
            Console.WriteLine("A dobások száma: " + dobasok.Count());
            Console.WriteLine("Az ösvények száma: " + osvenyek.Count());
            Console.WriteLine();
            //3. feladat
            Console.WriteLine("3. feladat");
            int maxLen = osvenyek.Max(x => x.Length);
            int maxI = osvenyek.FindIndex(y => y.Length == maxLen);
            Console.WriteLine($"Az egyik leghosszabb a(z) {maxI+1}. ösvény, hossza: {maxLen}");
            Console.WriteLine();
            //4. feladat
            Console.WriteLine("4. feladat");
            Console.Write("Adja meg egy ösvény sorszámát! ");
            int sorszam = int.Parse(Console.ReadLine());
            Console.Write("Adja meg a játékosok számát! ");
            int jatekosok = int.Parse(Console.ReadLine());
            Console.WriteLine();
            //5. feladat
            Console.WriteLine("5. feladat");
            string osveny = osvenyek[sorszam - 1];
            Console.WriteLine($"M: {osveny.Count(x =>x == 'M')} darab"); 
            Console.WriteLine($"V: {osveny.Count(x => x == 'V')} darab");
            Console.WriteLine($"E: {osveny.Count(x => x == 'E')} darab");
            Console.WriteLine();
            //6. feladat
            StreamWriter ir = new StreamWriter("kulonleges.txt");
            for (int i = 0; i < osveny.Length; i++)
            { 
                if (osveny[i] != 'M')
                {
                    ir.WriteLine($"{i + 1}\t{osveny[i]}");
                }
            }

            //7. feladat
            Console.WriteLine("7. feladat");
            int[] poz = new int[jatekosok];
            for (int i = 0; i < dobasok.Count(); i += 5)
            {
                poz=poz.Select((x,pozI) => x + dobasok[pozI+i] ));
            }
            









        }
    }
}
