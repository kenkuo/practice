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
			if parent not in progdict:
				progdict[parent] = None
			for child in children:
				progdict[child] = parent
		else:
			child = line.split()[0]
			if child not in progdict:
				progdict[child] = None
	print(progdict)
	print([k for k,v in progdict.items() if v == None])