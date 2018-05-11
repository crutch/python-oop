from math import pi

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

for tvar in tvary:
  print(tvar['typ'])

for i in range(0, len(tvary)):
  print(i, tvar['typ'])

for tvar in tvary:
  if tvar['typ'] == 'kruh':
    obsah = pi * tvar['polomer'] ** 2
    print(f'obsah kruhu je: {obsah}')
  elif tvar['typ'] == 'trojuholnik':
    obsah = tvar['zakladna'] * tvar['vyska'] / 2
    print(f'obsah trojuholnika je: {obsah}')
  elif tvar['typ'] == 'stvorec':
    obsah = tvar['strana'] ** 2
    print(f'obsah stvorca je: {obsah}')

celkovy_obsah = 0
for tvar in tvary:
  obsah = 0
  if tvar['typ'] == 'kruh':
    obsah = pi * tvar['polomer'] ** 2
  elif tvar['typ'] == 'trojuholnik':
    obsah = tvar['zakladna'] * tvar['vyska'] / 2
  elif tvar['typ'] == 'stvorec':
    obsah = tvar['strana'] ** 2
  celkovy_obsah = celkovy_obsah + obsah

print(f'celkovy obsah je: {celkovy_obsah}')
