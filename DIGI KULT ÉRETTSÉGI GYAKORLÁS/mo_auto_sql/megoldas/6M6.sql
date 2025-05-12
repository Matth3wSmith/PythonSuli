SELECT ut
FROM telepules
WHERE nev in (
SELECT nev FROM palya, telepules WHERE palya.ut = telepules.ut AND palya.ut = "M6"
) AND
ut <> "M6";
