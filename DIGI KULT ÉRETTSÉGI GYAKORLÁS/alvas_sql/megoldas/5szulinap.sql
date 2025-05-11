SELECT nev, lefekves
FROM diak d, alvas a, naptar n 
WHERE diakid=d.id 
    AND a.datum=n.datum 
    AND (MONTH(szuldatum)=MONTH(a.datum)) 
    AND DAY(szuldatum) = DAY(a.datum)-1
    AND melynap-1 IN (1,2,3,4,5);
    
---megoldokulcs
SELECT nev, lefekves 
FROM diak, alvas
WHERE diak.id = alvas.diakid
AND MONTH(szuldatum) = MONTH(datum-1)
AND DAY(szuldatum) = DAY(datum-1);