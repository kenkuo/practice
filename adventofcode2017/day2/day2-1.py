with open('day2input.txt', 'r') as f:
    input_data = f.read()
    total = 0
    for line in input_data.split("\n"):
        maxval = int(line.split()[0])
        minval = maxval
        for num in line.split():
            num = int(num)
            if num > maxval:
                maxval = num
            if num < minval:
                minval = num
        total = total + (maxval - minval)
    print (total)
