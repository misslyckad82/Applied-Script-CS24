# md5-hashcat.sh
I denna uppgift arbetar vi med hashvärden, lösenordsgenerering och lösenordsknäckning. 

Det modifierade Python-scriptet md5hasher.py genererar en output med tio (10) olika hashvärden. 
Scriptet genererar dock även lösenord till hasharna, men dessa lösenord syns ej som output. 
Dessa lösenord är tillräckligt långa för att inte kunna slås upp av en rainbow table.

Våra hashvärden används sedan som testdata i cracking-tester med hjälp av Hashcat.
Hashcat används för att knäcka hashade lösenord. 
Med hjälp av det enkla bash-scriptet md5-hashcat.sh kan vi utföra en MD5-cracking med Hashcat.
Det vill säga använda en mask för att brute-force de numeriska lösenorden.
