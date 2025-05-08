SELECT f.id, evszam
FROM fenykep f, kapcsolo, szemely sz
WHERE f.id=fenyid 
AND szemid=sz.id
AND evszam=szulev;