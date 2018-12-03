with open('day1input.txt', 'r') as f:
    input_data = f.read()
    total = 0
    half = int(len(input_data)/2)
    print(half)
    for idx,n in enumerate(input_data[:half]):
        if idx == len(input_data) - 1:
            if input_data[-1] == input_data[0]:
                total = total + int(input_data[0])
        else:
            if input_data[idx] == input_data[(idx+half)]:
                print(input_data[idx], input_data[(idx+half)%len(input_data)])
                total = total + int(input_data[idx])*2
                print(total)
    print(total)
    f.closed