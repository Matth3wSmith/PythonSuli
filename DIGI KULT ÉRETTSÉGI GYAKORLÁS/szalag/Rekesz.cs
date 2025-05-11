using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace szalag
{
    internal class Rekesz
    {
        public static int idoegyseg;
        public static int hossz;
        public int kezd;
        public int honnan;
        public int hova;
        public int tomeg;
        public bool atment0;
        public int vegez;
        public int sorszam;
        public Rekesz(int kezd, int honnan , int hova, int tomeg, int sorszam)
        {
            this.kezd= kezd;
            this.honnan= honnan ;   
            this.hova= hova ;
            this.tomeg = tomeg;
            this.sorszam = sorszam ;
            this.atment0 = honnan > hova && hova!=0;
            int tav = 0;
            if (this.atment0) { tav = hossz - honnan + hova; } else { tav = hova - honnan; }
            this.vegez = this.kezd + tav*idoegyseg;



        }
    }
}
