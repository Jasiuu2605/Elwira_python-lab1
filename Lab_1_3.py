import math

class Okrag:
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return round(2 * math.pi * self.promien, 2)

class Kolo(Okrag):
    def pole(self):
        return round(math.pi * self.promien ** 2, 2)


kolo_instancja = Kolo(10)

# Wywołanie
print("Obwód koła: ", kolo_instancja.obwod())
print("Pole koła: ", kolo_instancja.pole())
