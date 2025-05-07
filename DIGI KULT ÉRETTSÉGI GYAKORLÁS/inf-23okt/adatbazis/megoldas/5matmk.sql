/*SELECT evfolyam, betujel
FROM diak, jelentkezes, szakkor 
WHERE diak.azon=diakazon
    AND szakazon=szakkor.azon
    AND (evfolyam, betujel) IN (SELECT evfolyam,betujel 
                                FROM diak d, jelentkezes, szakkor sz 
                                WHERE d.azon=diakazon 
                                    AND szakazon=sz.azon
                                    AND mk = "Matematika")
GROUP BY evfolyam, betujel;*/

SELECT DISTINCT evfolyam, betujel
FROM diak, jelentkezes, szakkor 
WHERE diak.azon=diakazon
    AND szakazon=szakkor.azon
    AND mk = "Matematika"
ORDER BY 1,2;