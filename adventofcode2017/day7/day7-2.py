with open("day7input.txt", "r") as f:
    input_data = f.read()
    progdict = {}
    for line in input_data.split("\n"):
        print(line)
        arrow = line.find('>')
        if arrow > 0:
            children = line[arrow+2:].split(', ')
            print(children)
            parent = line[:arrow-2].split()[0]
            weight = int(line[:arrow-2].split()[1].strip("()"))
            progdict[parent] = (children, weight)
        else:
            child = line.split()[0]
            weight = int(line.split()[1].strip("()"))
            progdict[child] = (None, )

    print(progdict)



class prog:
    def __init__(self):
        self.children = []

    def totalweightonself:
        if len(self.children) is 0:
            return self.weight
        else:
            return sum(self.children) + self.weight

    def arechildrenbalanced:
        if len(set(self.children)) == 1:
            return True
        else:
            return False