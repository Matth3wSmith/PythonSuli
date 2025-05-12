SELECT palya.ut, kesz
FROM palya, vege, telepules
WHERE telepid = telepules.id AND telepules.ut = palya.ut AND palya.ut = vege.ut
ANd hatar = "Szlovákia";
