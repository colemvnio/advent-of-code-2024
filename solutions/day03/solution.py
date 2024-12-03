import re
from utils.input_reader import read_input_raw

# Idea: Extract each mul(x,y) operation from the *raw* input
# then calculate each extracted operation and add it to the total
def solve_part1(lines: list[str]) -> int:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
    
    total = 0

    for match in matches:
        total += int(match[0])*int(match[1])
    return total


# Idea: Similar to part 1, extract all operations, then evaluate do() or don't(), then RIGHT AFTER
# perform the operation by extracting x and y
def solve_part2(lines: list[str]) -> int:
    total = 0
    enabled = True
    operations = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", lines)
    
    for operation in operations:
        # Check for don't() and do(), and leverage elif to then operate based on previous eval
        if operation == "don't()":
            enabled = False
        elif operation == "do()":
            enabled = True
        elif enabled:
            # Extract x and y to multiply
            matches = re.findall(r"(\d+),(\d+)", operation)
            if matches:
                total += int(matches[0][0])*int(matches[0][1])
    
    return total

def main():
    lines = read_input_raw(3)
    
    part1_result = solve_part1(lines)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part2(lines)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()
