using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace jelado
{
    internal class Jel
    {
        public int hour;
        public int min;
        public int sec;
        public int x;
        public int y;
        public int sorszam;
        public TimeOnly time;
        public Jel(int ora, int perc, int sec, int x, int y, int sorszam)
        {
            this.hour = ora;
            this.min = perc;    
            this.sec = sec;
            this.x = x;
            this.y = y;
            this.sorszam = sorszam;
            this.time = new TimeOnly(ora,perc,sec);
            /*TimeSpan ido = new TimeOnly(ora, perc, sec + 1) - this.time;
            Console.WriteLine(ido.TotalSeconds);*/

        }
    }
}
