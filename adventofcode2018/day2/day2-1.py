from collections import defaultdict
with open('input.txt', 'r') as f:
  twice = 0
  thrice = 0
  for line in f:
    linedict = defaultdict(int)
    for c in line:
      linedict[c] += 1
    twiceline = False
    thriceline = False
    for k,v in linedict.items():
      if v == 2:
        twiceline = True
      if v == 3:
        thriceline = True
    if twiceline == True:
      twice += 1
    if thriceline == True:
      thrice += 1
  print(twice)
  print(thrice)
  print(twice*thrice)
    