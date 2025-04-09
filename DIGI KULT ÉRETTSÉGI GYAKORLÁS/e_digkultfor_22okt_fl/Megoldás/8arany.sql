SELECT 
    megye.nev,
    SUM(aerob.letszam) / megye.letszam
FROM 
    megye
JOIN 
    aerob ON megye.kod = mkod
GROUP BY 
    megye.nev
ORDER BY 
    arany DESC
LIMIT 1;