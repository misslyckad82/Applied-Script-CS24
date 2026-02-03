#!/bin/bash
#
# Detta script samlar in systeminformation - RECON
#
# Kan användas för följande attacker:
# En antagonist/hotaktör kan använda scriptet för informationsinsamling av Linux-system. 
# Hen kan sedan använda denna information för att hitta sårbarheter i systemet, såsom bristande uppdateringar. Och därigenom göra en riktad attack mot systemet och/eller nätverket.

# Som etisk hackare kan scriptet däremot användas som ett hjälpmedel vid penetrationstestning.
#
# Author: Sanna Rytilahti
# Last Update: 2026-02-03


echo "Välkommen till RECON script för att kontrollera en Linux-miljö"

echo
echo "=== SYSTEMINFO ==="
uname -a

echo
echo "=== AKTUELL ANVÄNDARE ==="
echo $USER

echo
echo "=== INLOGGADE ANVÄNDARE ==="
who

echo
echo "=== ANVÄNDARE MED SHELL ==="
grep "sh$" /etc/passwd

echo
echo "=== NÄTVERK ==="
ip a | grep inet

echo
echo "=== OPERATIVSYSTEM ==="
cat /etc/os-release

echo
echo "=== RAM-ANVÄNDNING ==="
free -h
 
echo
echo "=== CPU-ARKITEKTUR ==="
lscpu

echo
echo "=== SHELL-KONTON ==="
cat /etc/passwd | grep "sh$"

echo
echo "=== PRIVAT IP ==="
ip a

echo
echo "=== PUBLIK IP- OCH PLATSINFO ==="
curl https://ipapi.co/json/

echo
echo "=== ÖPPNA PORTAR ==="
ss -tuln

echo
echo "=== PROCESSER OCH RESURSANVÄNDNING ==="
top -b -n 1

echo
echo "=== SLUT PÅ KONTROLL ==="








