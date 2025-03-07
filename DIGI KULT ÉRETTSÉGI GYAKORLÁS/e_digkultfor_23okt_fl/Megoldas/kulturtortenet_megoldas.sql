--- 2. feladat --- 2csapatok ----

    SELECT nev 
    FROM csapat 
    WHERE nev LIKE "#%";
--- 3. feladat ---- 3csakegy ----

    SELECT nevado 
    FROM feladatsor 
    WHERE CHAR_LENGTH(nevado)=CHAR_LENGTH(REPLACE(nevado," ",""))+1;
    --- megoldókulcs
    SELECT nevado FROM feladatsor WHERE nevado NOT LIKE "% % %" AND nevado LIKE "% %";
    --- vagy
    SELECT nevado FROM feladatsor WHERE LOCATE(" ", SUBSTRING(nevado, LOCATE(" ", nevado)+1))=0 AND LOCATE(" ", nevado)<>0;
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
    SELECT nevado, COUNT(*)
        FROM feladatsor
            JOIN feladat ON feladatsor.id=feladatsorid
        WHERE feladat.id 
                NOT IN(
                    SELECT feladatid
                        FROM csapat
                            JOIN megoldas ON csapat.id=csapatid
                            right JOIN feladat ON feladat.id=feladatid
                        WHERE csapat.nev="#win"
                        )
        GROUP BY nevado;
--- 9. feladat ---- 9ugyanabban ----
    SELECT nevado FROM feladatsor WHERE MONTH(kituzes)=MONTH(hatarido);
    
    
    SELECT nevado  FROM feladatsor WHERE MONTH(kituzes)=MONTH(hatarido)       AND ag="irodalom"; 

--- 10. feladat ---- 10legrovidebb ----
    SELECT nevado FROM feladatsor WHERE DATEDIFF(hatarido,kituzes)=(SELECT MIN(DATEDIFF(hatarido,kituzes)) FROM feladatsor);

--- 11. feladat ---- 11rogton ----
    SELECT nevado,kituzes 
        FROM feladatsor AS folekerdezes 
        WHERE DATEDIFF(kituzes, 
            (SELECT hatarido 
                FROM feladatsor 
            WHERE id=folekerdezes.id-1)) =1;

    SELECT nevado,hatarido,kituzes 
        FROM feladatsor 
        WHERE kituzes IN
            (SELECT ADDDATE(hatarido,INTERVAL 1 DAY) FROM feladatsor);

    --- megoldókulcs ---
    SELECT kovetkezo.nevado, kovetkezo.kituzes FROM feladatsor AS kovetkezo, feladatsor AS elozo WHERE DATEDIFF(kovetkezo.kituzes, elozo.hatarido)=1; 

    SELECT nevado, elozo.hatarido FROM feladatsor, (SELECT hatarido FROM feladatsor) as elozo WHERE DATEDIFF(feladatsor.kituzes, elozo.hatarido)=1; 