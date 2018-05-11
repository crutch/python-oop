from math import pi

def obsah_kruhu(tvar):
  return pi * tvar['polomer'] ** 2

def obsah_stvorca(tvar):
  return tvar['strana'] ** 2

def obsah_trojuholnika(tvar):
  return tvar['zakladna'] * tvar['vyska'] / 2

def obsah_tvaru(tvar):
  if tvar['typ'] == 'kruh':
    return obsah_kruhu(tvar)
  elif tvar['typ'] == 'stvorec':
    return obsah_stvorca(tvar)
  elif tvar['typ'] == 'trojuholnik':
    return obsah_trojuholnika(tvar)

tvary = [
  {
    'typ': 'kruh',
    'polomer': 5
  },
  {
    'typ': 'trojuholnik',
    'zakladna': 5,
    'vyska': 2
  },
  {
    'typ': 'stvorec',
    'strana': 5
  }
]

celkovy_obsah = 0
for tvar in tvary:
  celkovy_obsah = celkovy_obsah + obsah_tvaru(tvar)

print(f'celkovy obsah je: {celkovy_obsah}')

# a teraz to pokazime
# tvary.append(
#   {
#     'typ': 'obdlznik',
#     'strany': [5,2]
#   }
# )
#
# celkovy_obsah = 0
# for tvar in tvary:
#   celkovy_obsah = celkovy_obsah + obsah_tvaru(tvar)
#
# print(f'celkovy obsah je: {celkovy_obsah}')

