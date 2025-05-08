SELECT nev, fenyid
    FROM szemely, kapcsolo
    WHERE id = szemid
    GROUP BY fenyid
    HAVING COUNT(szemid)=1;
