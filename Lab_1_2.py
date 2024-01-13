import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc(self, inny_punkt):
        return math.sqrt((self.x - inny_punkt.x) ** 2 + (self.y - inny_punkt.y) ** 2)


class Linia:
    def __init__(self, wierzcholki):
        self.wierzcholki = wierzcholki

    def dlugosc(self):
        dlugosc_linii = 0
        for i in range(len(self.wierzcholki) - 1):
            dlugosc_linii += self.wierzcholki[i].odleglosc(self.wierzcholki[i + 1])
        return dlugosc_linii

punkt1 = Punkt(-3, -2)
punkt2 = Punkt(1, 4)
punkt3 = Punkt(1, 1)

linia = Linia([punkt1, punkt2, punkt3])


print(linia.dlugosc())
