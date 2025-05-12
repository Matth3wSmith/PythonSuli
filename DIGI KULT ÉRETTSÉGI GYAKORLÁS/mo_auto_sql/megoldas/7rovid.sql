SELECT nev, t1.ut 
FROM telepules t1, vege v1
WHERE telepid=t1.id AND
nev = (SELECT nev FROM vege, telepules WHERE telepules.id=telepid AND v1.id <> vege.id AND vege.ut = v1.ut AND t1.nev=nev);

SELECT nev, ut FROM telepules WHERE id IN (SELECT telepid FROM vege GROUP BY telepid HAVING COUNT(id)>1);