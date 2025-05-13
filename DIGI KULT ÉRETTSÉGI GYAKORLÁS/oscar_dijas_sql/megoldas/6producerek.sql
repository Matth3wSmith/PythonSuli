SELECT nev, COUNT(ev) AS "jelolesek szama", MAX(ev)-MIN(ev) AS "eltelt ido"
FROM keszito, film, kapcsolat 
WHERE film.id=filmid AND keszitoid=keszito.id
AND producer
GROUP BY nev
HAVING COUNT(ev)>=2;