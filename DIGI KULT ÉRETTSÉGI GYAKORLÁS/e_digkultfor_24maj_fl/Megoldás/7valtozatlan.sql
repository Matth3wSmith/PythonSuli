SELECT kozterulet, hazszam, ar 
    FROM ingatlan JOIN hirdetes AS t1 ON ingatlan.id=ingatlanid 
    WHERE allapot = "meghirdetve" 
        AND ingatlanid IN (SELECT ingatlanid 
                                FROM hirdetes
                                WHERE t1.ingatlanid=ingatlanid 
                                    AND allapot = "eladva" 
                                    AND t1.ar = ar);