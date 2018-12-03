with open('day1input.txt', 'r') as f:
    input_data = f.read()
    total = 0
    for idx,n in enumerate(input_data):
        if idx == len(input_data) - 1:
            if input_data[-1] == input_data[0]:
                total = total + int(input_data[0])
        else:
            if input_data[idx] == input_data[idx+1]:
                total = total +int(input_data[idx])
    print(total)
    f.closed