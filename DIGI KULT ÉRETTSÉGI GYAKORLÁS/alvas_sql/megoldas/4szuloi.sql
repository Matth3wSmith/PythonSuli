SELECT datum 
FROM naptar 
WHERE datum = (SELECT ADDDATE(datum, INTERVAL 7 DAY) 
                FROM naptar
                WHERE melynap=2
                ORDER BY 1
                LIMIT 1);