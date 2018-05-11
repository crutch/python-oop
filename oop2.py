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


class Obdlznik:
  def __init__(self, strany):
    assert len(strany) == 2
    self.strany = strany

  def obsah(self):
    return self.strany[0] * self.strany[1]


class Stvorec(Obdlznik):
  def __init__(self, strana):
    super(Stvorec, self).__init__([strana, strana])


tvary = [
  Kruh(5),
  Trojuholnik(zakladna=5,vyska=2),
  Stvorec(5)
]

celkovy_obsah = 0
for tvar in tvary:
  celkovy_obsah = celkovy_obsah + tvar.obsah()

print(f'celkovy obsah je {celkovy_obsah}')

