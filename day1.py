import helper

def part1():
    input = helper.get_daily_input_numbers(1)

    previous = input[0]
    count = 0

    for line in input:
        if line > previous:
            count += 1
        previous = line
    
    return count

def part2():
    input = helper.get_daily_input_numbers(1)

    previous = input[0] + input[1] + input[2]
    count = 0
    index = 0

    while input:
        try:
            current_section = input[index] + input[index + 1] + input[index + 2]
            if current_section > previous:
                count += 1
            previous = current_section
            index += 1
        #we've hit the end of the array so lets finish
        except IndexError:
            break
    
    return count
        
if __name__ == "__main__":
    print("Answer to part 1: ", part1())
    print("Answer to part 2: ", part2())