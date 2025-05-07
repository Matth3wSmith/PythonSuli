using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace park
{
    internal class Felajanlas
    {
        public int kezd = 0;
        public int veg = 0;
        public char szin;
        public int agyasok = 0;
        public bool mindketOldal;
        public int sorszam;

        public Felajanlas(int kezd, int veg, char szin, int sorszam, int agyasSzam)
        {
            this.kezd = kezd;
            this.veg = veg;
            this.szin = szin;
            this.mindketOldal = veg < kezd;
            this.sorszam = sorszam;
            if (veg < kezd)
            {
                this.agyasok = agyasSzam - this.kezd + 1 + this.veg;
                /*Console.WriteLine(this.mindketOldal);
                Console.WriteLine(this.kezd+" "+this.veg);*/
            }
            else
            { 
                this.agyasok = this.veg-this.kezd+1;

            }
        }
    }
}
