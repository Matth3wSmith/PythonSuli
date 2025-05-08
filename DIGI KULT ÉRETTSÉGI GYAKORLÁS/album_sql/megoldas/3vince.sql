SELECT f.id, evszam-szulev AS eletkor, meret_x*meret_y AS meret 
FROM fenykep f, kapcsolo, szemely sz
WHERE f.id=fenyid 
AND szemid=sz.id
AND nev = "Vince";
