SELECT sz.nev AS "Szakkör", tanar AS "Tanár", d.nev AS "Diák",CONCAT(evfolyam,betujel) AS "Osztály"
FROM szakkor sz, jelentkezes, diak d 
WHERE d.azon=diakazon
    AND szakazon = sz.azon
    AND mk = "2. idegen nyelv"
ORDER BY 1, 3;