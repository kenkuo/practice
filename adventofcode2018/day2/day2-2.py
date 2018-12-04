def compare_words(a, b):
  same_letters = []
  for i,c in enumerate(a):
    if c == b[i]:
      same_letters.append(c)
  if len(same_letters) == len(a)-1:
    return same_letters
  else:
    return False
    

with open('input.txt', 'r') as f:
  data = f.read()
  for line in data.split():
    for line_inner in data.split():
      same = compare_words(line.strip(), line_inner.strip())
      if same:
        print(same)
        exit()
