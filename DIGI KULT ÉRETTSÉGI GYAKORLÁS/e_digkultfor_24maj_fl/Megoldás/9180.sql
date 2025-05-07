SELECT kozterulet, hazszam, SUM(
    IF(funkcio = 'terasz', (hossz * szel) * 0.5, hossz * szel)
) AS alapterulet
FROM ingatlan
JOIN helyiseg ON ingatlan.id = ingatlanid
GROUP BY ingatlan.id
HAVING alapterulet > 180;