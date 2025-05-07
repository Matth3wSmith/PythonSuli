SELECT sz.nev, tanar, mk, COUNT(diakazon) AS jelentkezo_szama
FROM szakkor sz, jelentkezes j
WHERE sz.azon=szakazon 
GROUP BY sz.nev
HAVING COUNT(diakazon)>=10;