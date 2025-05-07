SELECT nev, lefekves, szuldatum, a.datum
FROM diak d, alvas a, naptar n 
WHERE diakid=d.id 
    AND a.datum=n.datum 
    AND (MONTH(szuldatum)=MONTH(a.datum)) 
    AND DAY(szuldatum) = DAY(a.datum)-1
    AND melynap-1 IN (1,2,3,4,5);

