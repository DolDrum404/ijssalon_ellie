from algemene_functies import mijn_functie_2
from helper import decoreer

def aanbieding_1(smaak, prijs, korting):
    korting = prijs * (1 - korting)
# De volgende regel heb ik vanuit Google en is om 2 getallen achter de komma te krijgen (opmaak)
    korting = f"{korting:.2f}".replace('.',',')
    return print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.")

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
    return totaal

# De gegevens uit de opdracht
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

# Bereken het exclusief btw bedrag via de functie
uitvoer = inkomsten_totaal(week_inkomsten, btw)

# Bereken de btw en het bedrag inclusief btw (afgerond op 2 decimalen)
losse_btw = f"{uitvoer * btw:.2f}".replace('.',',')
# De volgende code is later misschien nodig
#totaal_incl_btw = f"{uitvoer * (1 + btw):.2f}".replace('.',',')

def laag_hoog(mijn_lijst):
    uitvoer =[]
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

laagste_bedrag, hoogste_bedrag = laag_hoog(week_inkomsten)

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    berekend_gemiddelde = totaal / aantal
    # Effe mooi maken met ,00
    berekend_gemiddelde = f"{berekend_gemiddelde:.2f}".replace('.',',')
    return f"De gemiddelde inkomsten deze week zijn {berekend_gemiddelde} euro."

def meervoudig(invoer_lijst):
    laagste, hoogste = laag_hoog(invoer_lijst)
    return [laagste, hoogste]

def combinatie(invoer_lijst_2):
    korte_lijst = laag_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

## ---------------------------
## Hierna volgen de antwoorden

decoreer("Antwoorden / Uitvoer")

## Teruggeefwaarde van de functie aanbieding_1 (antwoord opdracht 5)
aanbieding_1("aardbei", 4, 0.1)

print()

## Teruggeefwaarde van de functie inkomsten_totaal (antwoord opdracht 7)
print(f"Het totaal van alle inkomsten van deze week is {uitvoer} euro, waarover {losse_btw} euro btw betaald dient te worden.")

print()
## Teruggeefwaarde van de functie gemiddelde (antwoord opdracht 10)
print(gemiddelde(week_inkomsten))
