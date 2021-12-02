import helper

def part1():
    input = helper.get_daily_input_strings(2)

    horizontal = depth = 0

    for current in input:
        current = current.split()
        key = current[0]
        value = int(current[1])
        if key == "up":
            depth -= value
        if key == "down":
            depth += value
        if key == "forward":
            horizontal += value

    return horizontal * depth


def part2():
    input = helper.get_daily_input_strings(2)

    horizontal = depth = aim = 0

    for current in input:
        current = current.split()
        key = current[0]
        value = int(current[1])
        if key == "up":
            aim -= value
        if key == "down":
            aim += value
        if key == "forward":
            horizontal += value
            depth += (aim * value)

    return horizontal * depth
