import math

dagpris = {
    0: 0,
    1: 120,
    7: 280, 
    30: 505, 
    60: 1002, 
    90: 1503,
    180: 2505
}

# finn minste key større enn current dag
def neste_nivaa(current_dag, prisliste):
    #dictionary_items = prisliste.items()
    sortert = sorted(prisliste)
    for key in sortert:
        if(key > current_dag):
            return key
    return current_dag


def finn_billigste(antall_dager, prisliste):
    pris_for_n_dager = [["",0] for i in range(antall_dager+1)]
    for dag in range(0,antall_dager+1):
        if dag in prisliste: 
            pris_for_n_dager[dag] = [str(dag), prisliste[dag]]
            continue

        neste_pris_dag = neste_nivaa(dag, prisliste) 
        minst = prisliste[neste_pris_dag]

        alt1 = pris_for_n_dager[dag-1][1]+prisliste[1] #kun hvis vi er på dag 2 er denne relevant, kunne sikekrt gjort på en bedre måte <3
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
        
def skriv_ut_fint_hehe(antall_dager):
    fremgangsmåte, beløp = finn_billigste(antall_dager, dagpris)
    print("Periodebillettene du bør kjøpe for å spare mest på å reise i", antall_dager, "dager: ")
    print(fremgangsmåte)
    print("til en samlet verdi på", beløp, "kronasjer")

skriv_ut_fint_hehe(128)



