SELECT nev, fenyid
    FROM szemely, kapcsolo
    WHERE id = szemid
    GROUP BY fenyid
    HAVING COUNT(szemid)=1;


--megoldokulcs
SELECT nev, fenyid
FROM szemely, kapcsolo
WHERE id = szemid
AND fenyid in (SELECT fenyid
FROM kapcsolo
GROUP BY fenyid
HAVING COUNT(*)=1)
AND nev is not NULL;