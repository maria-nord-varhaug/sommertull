# sommertull

I bussats kan du regne ut hvilken kombinasjon av periodebilletter du bør kjøpe i atb for å minimalisere pengebruk for en gitt periode under 180 dager. 
Du kan velge aldersgruppe og hvor mange soner du skal reise gjennom, men for øyeblikket fungerer det kun for 1 sone.

Ettersom atb ikke hadde noe api for prisene deres er jsonfilen min veldig statisk og inneholder mest sannsynlig feil siden jeg førte inn i den selv, og vil dessverre heller ikke oppdatere seg når de endrer billettpriser.

Selve algoritmen er en grei dynamisk en, der vi kjører iterativt gjennom billettlengde - starter på perioder på 1 dag og bygger seg videre frem til den når ønsket periode. 
