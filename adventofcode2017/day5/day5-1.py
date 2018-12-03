with open("day5input.txt", "r") as f:
    input_data = f.readlines()
    cur_index = 0
    prev_index = 0
    steps = 0
    my_data = [int(num) for num in input_data]
    while((cur_index >= 0) and (cur_index < len(input_data))):
        prev_index = cur_index
        cur_index += my_data[cur_index]
        if(my_data[prev_index] >= 3):
            my_data[prev_index] -= 1
        else:
            my_data[prev_index] += 1
        steps += 1
    print(steps)