#!/usr/bin/env python3

# Script för att kontrollera om antivirusprogram i Windows-miljö reagerar på EICAR-signaturen.

import platform
system = platform.system()

if system == "Windows":
    print("Windows upptäckt. Scriptet fortsätter...")

elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows. Avbryter körning.")
    exit()

elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows. Avbryter körning.")
    exit()

else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    exit()

# Skriv EICAR-signaturen. Innehållet är helt ofarligt och kommer inte att skada systemet.
eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# För att garanterat trigga AV använder jag ändelsen .com på filen som skrivs.
# När jag öppnar den skapade filen innehållandes EICAR-strängen tolkar AV det som att jag försöker köra ett DOS-program med skadlig kod.
with open(r"C:\Users\missc\Documents\AV-TEST-NOT-DANGEROUS.com", "w") as f:
    f.write(eicar_str)
print("EICAR-strängen sparad som AV-TEST-NOT-DANGEROUS.COM. Windows AV bör reagera och sätta filen i karantän!")

import time

# Siffran inom parentes anger en fördröjning i antal sekunder som AV hinner analysera filen och vid behov ta bort den.
time.sleep(10)

try:
    with open(r"C:\Users\missc\Documents\AV-TEST-NOT-DANGEROUS.com", "r") as f:
        fil_innehåll = f.read()

    # Kontrollera om filens innehåll matchar EICAR-signaturen.
    if fil_innehåll == eicar_str:
        print("Filen kunde läsas. Antivirusprogrammet har inte blockerat den!")

except Exception as e:
    # Om ett fel uppstår här på grund av att filen har tagits bort eller flyttats.
    print("[!!!] Filen kunde inte läsas!")
    print("[!!!] Antivirusprogrammet har tagit bort/karantänat filen.")
    print("[---] Din AV/EDR-lösning är helt fungerande och skyddar mot kända virus-signaturer.")
