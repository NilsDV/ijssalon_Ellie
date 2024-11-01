from helper import decoreer

def print_aanbieding():
    prijzen={
        "aardbei" : "3",
        "vanille" : "4",
        "chocolade" : "5"
    }
    A= int(prijzen["aardbei"])
    aanbieding= A*0.8
    reclame_tekst= (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}")
    reclame_tekst2= reclame_tekst[:61]
    reclame_tekst3= (reclame_tekst2.upper())
    reclame_tekst4= (reclame_tekst3.split())
    for i in (reclame_tekst4):
        if len(i) >= 5:
            print(i.upper()) and print(i.lower())
        else:
            print(i.lower()) and print(i.upper())

decoreer("aanbieding")
print_aanbieding()