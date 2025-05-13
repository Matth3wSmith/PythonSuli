SELECT DISTINCT nev , filmid
FROM keszito keszit1, kapcsolat kapcs1
WHERE keszitoid=keszit1.id 
AND filmid IN (SELECT filmid FROM keszito, kapcsolat WHERE keszitoid=keszito.id AND nev = "Clint Eastwood")
AND nev <> "Clint Eastwood";