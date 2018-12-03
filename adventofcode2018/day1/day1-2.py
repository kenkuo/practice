with open('input.txt', 'r') as f:
    total = 0
    s = set()
    found = False
    while found == False:
      for num in f:
        total += int(num)
        if total in s:
          print("found duplicate total")
          print(total)
          found = True
          break
        else:
          s.add(total)
      f.seek(0)
