import os
import helper

if __name__ == "__main__":
    #find the latest python file
    current = 0
    for file in os.listdir(r'./'):
        if file.endswith(".py") and file.startswith("day"):
            day = int(file[3:file.find(".py")])
            if day > current:
                current = day

    #let the helper know what day we're using
    helper.current_day = current
    
    #dynamically import the latest python day file
    module = __import__("day" + str(current), globals(), locals(), [])
    print("Answer to part 1: ", module.part1())
    print("Answer to part 2: ", module.part2())