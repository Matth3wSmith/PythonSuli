SELECT datum 
FROM naptar 
WHERE datum = (SELECT ADDDATE(datum, INTERVAL 7 DAY) 
                FROM naptar
                WHERE melynap=2
                ORDER BY 1
                LIMIT 1);
---megoldokulcs
SELECT datum FROM naptar WHERE melynap = 2 ORDER BY datum LIMIT 1,1;
---megoldokulcs
SELECT datum 
FROM naptar 
WHERE datum > (SELECT MIN(datum) FROM naptar WHERE melynap = 2)
AND melynap = 2
ORDER BY datum
LIMIT 1;
