SELECT nev, AVG((24-HOUR(lefekves)-1)+((60-MINUTE(lefekves))/60)+((60-SECOND(lefekves))/3600)+HOUR(felkeles)+MINUTE(felkeles)/60+SECOND(felkeles)/3600) AS atlag 
FROM diak, alvas
WHERE diak.id=diakid
GROUP BY diak.id
HAVING atlag<8;
---megoldokulcs
SELECT nev, AVG(24-HOUR(lefekves)-MINUTE(lefekves)/60+HOUR(felkeles)+MINUTE(felkeles)/60) AS atlag
FROM diak, alvas
WHERE diak.id = alvas.diakid
GROUP BY nev
HAVING atlag<8;
