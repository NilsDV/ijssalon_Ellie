smaak= "aardbei"
prijs=4
korting=4-4*0.1
def aanbieding_1(smaak, prijs, korting):
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro")

inkomsten=[220, 430, 125, 160, 205, 90, 345]
totaal= sum(inkomsten)
bedrag= totaal*0.09
def inkomsten_totaal(totaal, bedrag):
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

mijn_lijst= [220, 430, 125, 160, 205, 90, 345]
def hoog_en_laag(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

gemiddelde_berekening= sum(mijn_lijst) / len(mijn_lijst)
def gemiddelde(mijn_lijst):
    return (f"De gemiddelde inkomsten van deze week zijn {gemiddelde_berekening} euro.")

invoer_lijst= [10, 5, 3, 2, 1, 2, 9] 
def hoog_en_laag(invoer_lijst):
    return max(invoer_lijst),min(invoer_lijst)
def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

from algemene_functies import mijn_functie_2
invoer_lijst_2 = [4, 7, 2, 9] 
#Ik heb mijn eigen lijst gebruikt omdat ik niet zeker wist of ik een specifieke lijst moest gebruiken.
def combinatie(invoer_lijst_2):
    korte_lijst= hoog_en_laag(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])