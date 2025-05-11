using System.ComponentModel.DataAnnotations;
using System.Xml;
using System.Xml.Serialization;

namespace jelado
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Kezdés 15:50 szunet 16:46 vissza: 16:58 vége 17:04 => 62 => 1 óra 2 perc
            //1 .feladat
            StreamReader olvas = new StreamReader("jel.txt");
            List<Jel> jelek = new List<Jel>();
            int sorszam = 1;
            while (!olvas.EndOfStream)
            {
                string[] vag = olvas.ReadLine().Split(" ");
                jelek.Add(new Jel(int.Parse(vag[0]), int.Parse(vag[1]), int.Parse(vag[2]), int.Parse(vag[3]), int.Parse(vag[4]), sorszam));
                sorszam++;
            }
            olvas.Close();

            //2. feladat
            Console.WriteLine("2. feladat");
            Console.Write("Adja meg a jel sorszámát! ");
            int kertSor = int.Parse(Console.ReadLine());
            Jel kertJel = jelek.Where(x => x.sorszam == kertSor).First();
            Console.WriteLine($"x={kertJel.x} y={kertJel.y}");
            Console.WriteLine();

            //4. feladat
            Console.WriteLine("4. feladat");
            Console.WriteLine("Időtartam: " + new TimeSpan(0,0,eltelt( jelek[jelek.Count()-1].time, jelek[0].time)));
            Console.WriteLine();
            //5. feladat
            Console.WriteLine("5. feladat");
            var xErtekek = jelek.Select(jel => jel.x);
            var yErtekek = jelek.Select(jel => jel.y);

            Console.WriteLine($"Bal alsó: {xErtekek.Min()} {yErtekek.Min()}, jobb felső: {xErtekek.Max()} {yErtekek.Max()}");
            Console.WriteLine();

            //6. feladat
            Console.WriteLine("6. feladat");
            double elmozdulas = 0;
            for (int i = 0; i < jelek.Count()-1; i++)
            {
                elmozdulas += Math.Sqrt(Math.Pow(jelek[i].x - jelek[i + 1].x,2)+ Math.Pow(jelek[i].y - jelek[i + 1].y, 2));
            }
            Console.WriteLine($"Elmozdulás: {Math.Round(elmozdulas,3)} egység");

            //7. feladat


            StreamWriter ir = new StreamWriter("kimaradt.txt");

            for (int i = 0; i < jelek.Count() - 1; i++)
            {
                int xElteres = Math.Abs(jelek[i + 1].x - jelek[i].x);
                int yElteres = Math.Abs(jelek[i + 1].y - jelek[i].y);
                int idoElteres = eltelt(jelek[i + 1].time, jelek[i].time);
                if (xElteres > 10 || yElteres > 10 || idoElteres > 5*60 ){
                    int koordElteresMiatt = 0;
                    double idoElteresMiatt = (idoElteres/60.0) / 5;
                    /*Console.WriteLine(jelek[i+1].time);
                    Console.WriteLine(idoElteres/60);
                    Console.WriteLine(idoElteresMiatt);
                    Console.WriteLine("x "+ xElteres +" y "+yElteres);*/


                    if (xElteres > yElteres)
                    {
                        koordElteresMiatt = xElteres / 10;
                    }
                    else {
                        koordElteresMiatt = yElteres / 10;
                    }

                    //Console.WriteLine(koordElteresMiatt);
                    if (koordElteresMiatt > idoElteresMiatt)
                    {
                        ir.WriteLine($"{jelek[i + 1].hour} {jelek[i + 1].min} {jelek[i + 1].sec} koordináta-eltérés {koordElteresMiatt}");
                    }
                    else { 
                        ir.WriteLine($"{jelek[i + 1].hour} {jelek[i + 1].min} {jelek[i + 1].sec} időeltérés {idoElteresMiatt}"); 
                    }

                }
            }

            ir.Close();

        }
        //3. feladat
        static int eltelt(TimeOnly ido1, TimeOnly ido2)
        {
            TimeSpan kulonbseg = (ido1 - ido2);
            return (int)kulonbseg.TotalSeconds;
        }
    }
}
