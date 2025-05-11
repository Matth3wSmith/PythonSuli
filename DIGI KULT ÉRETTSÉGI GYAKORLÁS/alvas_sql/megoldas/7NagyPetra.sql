SELECT d2.nev
FROM diak d2
JOIN alvas a2 ON d2.id = a2.diakid
JOIN alvas ap ON ap.diakid = (SELECT id FROM diak WHERE nev = 'Nagy Petra') AND a2.datum = ap.datum
WHERE a2.felkeles < ap.felkeles
GROUP BY d2.id, d2.nev
HAVING COUNT(*) = (SELECT COUNT(DISTINCT datum) FROM alvas);

SELECT d2.nev
FROM diak d2
WHERE d2.nev <> 'Nagy Petra'
AND NOT EXISTS (
    SELECT 1
    FROM alvas a2
    JOIN alvas ap 
      ON a2.datum = ap.datum
    WHERE a2.diakid = d2.id
      AND ap.diakid = (SELECT id FROM diak WHERE nev = 'Nagy Petra')
      AND a2.felkeles >= ap.felkeles
);

-- megoldokulcs
SELECT nev 
FROM diak
WHERE nev NOT IN 
(SELECT d1.nev 
FROM diak d1, alvas a1, diak d2, alvas a2
WHERE d1.id=a1.diakid AND d2.id=a2.diakid
AND d2.nev="Nagy Petra"
AND a1.datum = a2.datum
AND a1.felkeles >= a2.felkeles);