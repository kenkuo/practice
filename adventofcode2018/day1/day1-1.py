with open('input.txt', 'r') as f:
    total = 0
    for num in f:
      total += int(num)
    print (total)
