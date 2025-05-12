SELECT nev, COUNT(palya.ut) AS "autopalyak szama"
FROM telepules, palya
WHERE palya.ut=telepules.ut AND nev <> "Budapest"
GROUP BY nev
ORDER BY 2 DESC
LIMIT 1;  