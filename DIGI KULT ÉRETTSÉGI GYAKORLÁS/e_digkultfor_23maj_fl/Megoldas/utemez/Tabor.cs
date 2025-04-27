using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace utemez
{
    internal class Tabor
    {
        public int kezdHo = 0;
        public int kezdNap = 0;
        public int vegHo = 0;
        public int vegNap = 0;
        public string nevek = "";
        public string tema = "";
        public Tabor(int kezdHo, int kezdNap, int vegHo , int vegNap, string nevek, string tema)
        { 
            this.kezdHo = kezdHo;
            this.kezdNap = kezdNap;
            this.vegHo = vegHo;
            this.vegNap = vegNap;
            this.nevek = nevek;
            this.tema = tema;
        }
        public string datum()
        {
            return $"{this.kezdHo}.{this.kezdNap}-{this.vegHo}.{this.vegNap}.";
        }
    }
}
