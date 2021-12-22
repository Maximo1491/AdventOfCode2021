import helper

def part1():
    input = helper.get_daily_input_strings()
    gamma = epsilon = ''
    count1 = count0 = 0
    for i in range(len(input[0])):
        for number in input:
            if number[i] == '1':
                count1 += 1
            else:
                count0 += 1
        
        if count1 > count0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

        count0 = count1 = 0

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon

def part2():
    input = helper.get_daily_input_strings()

    oxy_count1 = oxy_count0 = co2_count1 = co2_count0 = 0
    oxygen = co2 = ''
    oxy_input = co2_input = input
    for i in range(len(input[0])):
        for number in oxy_input:
            if number[i] == '1':
                oxy_count1 += 1
            else:
                oxy_count0 += 1

        if oxy_count0 > oxy_count1:
            search = '0'
        else:
            search = '1'
        
        new_input = []
        for number in oxy_input:
            if number[i] == search:
                new_input += [number]

        if len(new_input) == 1:
            oxygen = new_input[0]

        oxy_input = new_input
        oxy_count0 = oxy_count1 = 0

        for number in co2_input:
            if number[i] == '1':
                co2_count1 += 1
            else:
                co2_count0 += 1

        if co2_count0 > co2_count1:
            search = '1'
        else:
            search = '0'
        
        new_input = []
        for number in co2_input:
            if number[i] == search:
                new_input += [number]

        if len(new_input) == 1:
            co2 = new_input[0]

        co2_input = new_input
        co2_count0 = co2_count1 = 0
    
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)

    return oxygen * co2
