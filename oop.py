from math import pi

class Kruh:
  def __init__(self, polomer):
    self.polomer = polomer

  def obsah(self):
    return pi * self.polomer ** 2


class Trojuholnik:
  def __init__(self, zakladna, vyska):
    self.zakladna = zakladna
    self.vyska = vyska

  def obsah(self):
    return self.zakladna * self.vyska / 2


class Stvorec:
  def __init__(self, strana):
    self.strana = strana

  def obsah(self):
    return self.strana ** 2


tvary = [
  Kruh(5),
  Trojuholnik(zakladna=5,vyska=2),
  Stvorec(strana=5)
]

celkovy_obsah = 0
for tvar in tvary:
  celkovy_obsah = celkovy_obsah + tvar.obsah()

print(f'celkovy obsah je {celkovy_obsah}')

