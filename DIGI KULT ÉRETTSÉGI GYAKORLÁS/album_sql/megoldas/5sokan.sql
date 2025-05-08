SELECT DISTINCT f.id, evszam 
FROM fenykep f, kapcsolo, szemely sz
WHERE f.id=fenyid 
AND szemid=sz.id
AND f.id = (SELECT f2.id FROM fenykep f2, kapcsolo, szemely sz2
                WHERE f2.id=fenyid 
                AND szemid=sz2.id
                GROUP BY f2.id
                ORDER BY COUNT(nev) DESC
                LIMIT 1);

