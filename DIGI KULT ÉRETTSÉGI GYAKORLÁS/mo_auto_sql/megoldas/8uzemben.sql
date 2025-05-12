SELECT palya.ut AS "Autópálya", kesz AS "Üzemhossz(km)", nev AS "Érintett települések" 
FROM palya, telepules
WHERE palya.ut = telepules.ut AND kesz <> 0;