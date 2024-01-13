import math

def kolo(promien):

    obwod = round(2 * math.pi * promien, 2)
    pole = round(math.pi * promien ** 2, 2)

    wyniki = {'obwód': obwod, 'pole': pole}

    return wyniki



promien = 7

wynik = kolo(promien)
print(wynik)
