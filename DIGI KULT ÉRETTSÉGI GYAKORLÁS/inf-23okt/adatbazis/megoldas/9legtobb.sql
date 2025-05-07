SELECT evfolyam, betujel, COUNT(DISTINCT sz.azon) AS kulonbozo
FROM szakkor sz, jelentkezes, diak d 
WHERE d.azon=diakazon
    AND szakazon = sz.azon
GROUP BY evfolyam,betujel
ORDER BY 3 DESC 
LIMIT 1;
