def find_divisible(line):
    print(line + "\n")
    for i in line.split():
        i = int(i)
        for j in line.split():
            print("i: " + str(i) + " j: " + str(j))
            j = int(j)
            if i == j:
                continue
            if (i%j) == 0:
                return int( i / j)
                break
            if (j%i) == 0:
                return int (j / i)
    return 0

with open('day2input.txt', 'r') as f:
    input_data = f.read()
    total = 0
    for line in input_data.split("\n"):
        total = total + find_divisible(line)
    print (total)

