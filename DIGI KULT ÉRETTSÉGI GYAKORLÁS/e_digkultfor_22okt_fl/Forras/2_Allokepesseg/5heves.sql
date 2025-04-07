SELECT COUNT(nev) FROM megye WHERE letszam < (SELECT letszam FROM megye WHERE nev = "Heves");
