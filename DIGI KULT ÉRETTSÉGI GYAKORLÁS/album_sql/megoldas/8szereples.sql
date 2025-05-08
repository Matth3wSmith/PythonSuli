SELECT evszam AS "Év", nev AS "Név", COUNT(nev) AS Darab 
FROM fenykep f,kapcsolo, szemely sz
WHERE f.id=fenyid 
    AND sz.id=szemid 
    AND nev IS NOT NULL
    GROUP BY evszam, nev;