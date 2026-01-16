Detta Python-script används för att kontrollera vilket operativsystem som scriptet körs på.

Om scriptet körs på en Windows-klient skrivs dessutom en EICAR-testfil, innehållandes EICAR-signaturen, för malware-detektion.
Detta ska trigga Windows-klientens antivirusprogram att sätta den skrivna filen i karantän, alternativt ta bort filen.
 
För att testa scriptet i Kali Linux-terminalen skriv "python3 av-test-med-eicar.py".
