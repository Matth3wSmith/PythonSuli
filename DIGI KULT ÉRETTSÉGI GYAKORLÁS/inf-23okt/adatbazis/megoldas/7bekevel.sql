SELECT sz.nev, d.nev
FROM szakkor sz, jelentkezes, diak d 
WHERE d.azon=diakazon
    AND szakazon = sz.azon
    AND (evfolyam, betujel, sz.nev) IN (SELECT evfolyam, betujel, sz2.nev
                                            FROM diak d2, jelentkezes, szakkor sz2
                                            WHERE d2.azon=diakazon
                                            AND szakazon = sz2.azon
                                            AND d2.nev = "Beke Fanni")
    AND d.nev <> "Beke Fanni";

/*SELECT evfolyam, betujel, sz2.nev
FROM diak d2, jelentkezes, szakkor sz2
WHERE d2.azon=diakazon
AND szakazon = sz2.azon
AND d2.nev = "Beke Fanni";*/