def check_factor(input_list, multiply):
    output_list = []
    while input_list != []:
        if input_list[0] % multiply == 0:
            output_list.append(input_list[0])
        input_list.pop(0)
    print(output_list)

list = [1,4,6,7,15,22,35]
multiply = 5
check_factor(list, multiply)

