SELECT fenyid, evszam
FROM fenykep f,kapcsolo, szemely sz
WHERE f.id=fenyid 
    AND sz.id=szemid 
    AND nev = "Anna" 
    AND "Matyi" IN (SELECT nev 
                        FROM szemely, kapcsolo
                        WHERE id = szemid AND f.id=fenyid AND nev="Matyi");
--megoldokulcs
SELECT id, evszam
FROM fenykep 
WHERE 
     id IN (SELECT fenyid 
                        FROM szemely, kapcsolo
                        WHERE id = szemid AND nev="Anna")
    AND id IN (SELECT fenyid 
                        FROM szemely, kapcsolo
                        WHERE id = szemid AND nev="Matyi");