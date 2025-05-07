SELECT sz.nev, evfolyam 
FROM szakkor sz, jelentkezes, diak d 
WHERE d.azon=diakazon
    AND szakazon = sz.azon
    AND (SELECT COUNT(evfolyam) 
            FROM szakkor sz2, jelentkezes, diak d 
            WHERE d.azon=diakazon
                AND szakazon = sz2.azon
                AND sz.nev=sz2.nev
                AND evfolyam NOT IN (10,11))=0;