with open('day4input.txt') as f:
	input_data = f.read()
	total = 0
	for line in input_data.split("\n"):
		unique = []
		for word in line.split():
			word = ''.join(sorted(word))
			if(word in unique):
				print("dupe")
				continue
			else:
				unique.append(word)
		if len(unique) == len(line.split()):
			print(unique)
			print(line.split())
			total += 1
	print (total)
