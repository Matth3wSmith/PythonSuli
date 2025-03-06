--- 2. feladat --- 2heltai ---
    SELECT cim, eredeti FROM film  WHERE magyarszoveg="Heltai Olga";

--- 3. feladat --- 3szinkrend ---




--- 8. feladat --- 8rendszin ---
    SELECT DISTINCT rendezo AS "Színész-rendező" FROM film AS folekerdezes WHERE rendezo IN(SELECT szinesz FROM szinkron WHERE szinesz=folekerdezes.rendezo);

--- 9. feladat --- 9pap ---
    SELECT cim, hang 
        FROM szinkron 
            JOIN film ON film.filmaz=szinkron.filmaz 
        WHERE szinkron.filmaz IN
            (SELECT film.filmaz 
                FROM film JOIN szinkron ON film.filmaz=szinkron.filmaz 
                WHERE hang="Pap Kati") 
            AND hang != "Pap Kati" 
        ORDER BY 1, 2;

--- 10. feladat --- 10harom ---
    SELECT szinesz, hang, COUNT(*) FROM szinkron GROUP BY szinesz HAVING COUNT(*)>=3 ORDER BY 3 DESC;

--- 11. feladat --- 11egyev ---
    SELECT ev, hang 
        FROM film as fo, join szinkron on film.filmaz=szinkron.filmaz
        WHERE (ev,hang)
            IN
            (SELECT ev, hang 
                FROM szinkron 
                    JOIN film 
                        ON film.filmaz=szinkron.filmaz 
                WHERE studio!="Mafilm Audio Kft." and ev=fo.ev);



