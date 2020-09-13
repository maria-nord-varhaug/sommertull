import math
import json

# henter fra json fil med data på form 
# "aldersgruppe": {
#   "0 dager periodebillett": [pris for 1 sone, 2 soner, 3 soner, 4 soner, 5-13 soner],
#   "1 dag periodebillett":[...], 
#   "7 dager periodebillett": [...], 
#   ... ,
# }

def generelle_billettpriser():
    data = {}
    # hent inn data 
    with open('bussatser.json', 'r') as minfil:
        data = minfil.read()

    # parse til python
    obj = json.loads(data)
    return obj

# tar inn hvilken aldersgruppe man vil ha billettpriser for (voksen, honnør, barn eller student) samt hvor mange soner man vil reise i (1, 2, 3,4,5-13)
# og lagrer alle billettpriser i dagpris-dicten

def spesifikke_billettpriser(aldersgruppe, antall_soner): 
    dagpris = {} # dict på form {"0": 0, "1": 120, "7": 280, ..., "billettvarihet i dager": pris basert på hvilke data brukeren har gitt}
    billettsatser = generelle_billettpriser()
    for periode, sonepriser in billettsatser[aldersgruppe].items():   
        dagpris[periode] = sonepriser[antall_soner-1] # sett inn i dagpris-dicten basert på json. sonepriser er 1-indeksert siden vi begynner på sone 1.
    return dagpris


# finn minste key større enn current dag
def neste_nivaa(current_dag, prisliste):
    #dictionary_items = prisliste.items()
    sortert = sorted(prisliste)
    for key in sortert:
        if(int(key) > current_dag):
            return key
    return current_dag


def finn_billigste(antall_dager, prisliste):
    # må bruke ["",0] istedetfor bare 0 for å lagre kombinasjonen av billetter som er billigst i tekst, så vi ikke bare ender opp med beløpet
    if(str(antall_dager) in prisliste ):
        return [str(antall_dager), prisliste[str(antall_dager)]]
    pris_for_n_dager = [["",0] for i in range(antall_dager+1)]  # todimensjonal liste som er <antall dager man vil finne billigste billetkobinasjon av> lang
    for dag in range(0,antall_dager+1):
        if str(dag) in prisliste: 
            pris_for_n_dager[dag] = [str(dag), prisliste[str(dag)]]
            continue

        neste_pris_dag = neste_nivaa(dag, prisliste) 
        minst = prisliste[neste_pris_dag]

        alt1 = pris_for_n_dager[dag-1][1]+prisliste['1'] #kun hvis vi er på dag 2 er denne relevant, kunne sikekrt gjort på en bedre måte <3
        if alt1 < minst:
            minst = alt1
            neste_pris_dag = pris_for_n_dager[dag-1][0] + " + " + str(1)
        
        for i in range(1, math.ceil(dag/2)+1):
            alt1 = pris_for_n_dager[dag-i][1]+pris_for_n_dager[i][1]
            if(alt1 <= minst):
                minst = alt1
                neste_pris_dag = str(pris_for_n_dager[dag-i][0]) + " + " + str(pris_for_n_dager[i][0])

        pris_for_n_dager[dag] = [neste_pris_dag, minst]
    return pris_for_n_dager[antall_dager]
        
def skriv_ut_fint_hehe():
    aldersgrupper = ["voksen", "honnor", "barn", "student"]
    while(True):
        valgt_aldersgruppe = int(input("hvilken aldersgruppe er du? Skriv 0 for voksen, 1 for honnør, 2 for barn, 3 for student.\n>"))
        antall_dager = int(input("hvor mange dager trenger du kollektivtransport for? atb tilbyr ikke lenger periode enn 180 dager så skriv et tall mellom 0 og 180.\n>"))
        antall_soner = int(input("hvor mange soner vil du ha billett for? Skriv 1, 2, 3, 4 eller 5 (der 5 står for 5-13, da atb tar samme pris for disse)\n>"))
        if((0 <= int(valgt_aldersgruppe) <= 3) and (0 <= int(antall_dager) <= 180) and (1 <= int(antall_soner) <= 5)):
            break
    valgt_aldersgruppe = aldersgrupper[int(valgt_aldersgruppe)]
    dagpris = spesifikke_billettpriser(valgt_aldersgruppe,antall_soner)

    fremgangsmåte, beløp = finn_billigste(antall_dager, dagpris)
    if(beløp == None):
        print("Det finnes ikke dagsbilletter for å reise i mer enn en sone. En enkeltbillett for ")
    print("Periodebillettene du bør kjøpe for å spare mest på å reise i", antall_dager, "dager: ")
    print(fremgangsmåte)
    print("til en samlet verdi på", beløp, "kronasjer")

skriv_ut_fint_hehe()
