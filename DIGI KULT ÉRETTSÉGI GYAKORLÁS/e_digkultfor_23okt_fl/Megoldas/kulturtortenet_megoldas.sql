--- 2. feladat --- 2csapatok ----

    SELECT nev FROM csapat 
        WHERE nev LIKE "#%";
--- 3. feladat ---- 3csakegy ----

    SELECT nevado FROM feladatsor 
        WHERE CHAR_LENGTH(nevado)==CHAR_LENGTH(REPLACE(nevado," ",""))+1;
--- 4. feladat ---- 4szilveszter ----

    SELECT nevado
        FROM feladatsor 
        WHERE kituzes<"2018-12-31" AND hatarido>"2018-12-31";
--- 5. feladat ---- 5eredmeny ----
    SELECT nev, SUM(pontszam) 
        FROM csapat 
            INNER JOIN megoldas ON csapatid=csapat.id 
        GROUP BY nev 
        ORDER BY 2 DESC;
--- 6. feladat ---- 6nem150 ----

    SELECT nevado, ag, SUM(pontszam) 
    FROM feladatsor 
        INNER JOIN feladat ON feladatsorid=feladatsor.id 
    GROUP BY feladatsorid
    HAVING SUM(pontszam)!=150;

--- 7. feladat ---- 7hibatlan ----
    SELECT DISTINCT nev FROM csapat JOIN megoldas ON csapat.id=csapatid JOIN feladat ON feladatid=feladat.id WHERE feladat.pontszam=megoldas.pontszam;

--- 8. feladat ---- 8#win ----
    SELECT feladatsor.id,COUNT(feladatsorid) FROM feladat JOIN feladatsor ON feladatsor.id=feladatsorid GROUP BY feladatsor.id;

    SELECT feladat.id, megoldas.id FROM feladat LEFT JOIN megoldas ON feladat.id=feladatid JOIN csapat ON csapat.id=csapatid WHERE megoldas.id IS NULL;

    SELECT feladat.id, megoldas.id FROM csapat JOIN megoldas ON csapat.id=csapatid RIGHT JOIN feladat ON feladat.id=feladatid WHERE megoldas.id IS NULL;



    SELECT feladat.id, megoldas.id FROM feladat, csapat LEFT JOIN megoldas ON csapatid=csapat.id;
