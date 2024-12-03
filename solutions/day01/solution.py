from utils.input_reader import read_input_lines

# Idea: Create two lists, one for the left side and one for the right side
# then sort them and loop over them to calculate the total distance
def solve_part1(lines: list[str]) -> int:
    left_side = []
    right_side = []
    
    for line in lines:
        left, right = map(int, line.strip().split())
        left_side.append(left)
        right_side.append(right)
    
    left_side.sort()
    right_side.sort()
    
    total_distance = 0

    # Loop over each pair, and calculate the total distance
    for left, right in zip(left_side, right_side):
        distance = abs(left - right)
        total_distance += distance
    
    return total_distance

# Idea: Create both lists, then count occurrences for each left number in the right list
# then calculate the total score
def solve_part2(lines: list[str]) -> int:
    left_side = []
    right_side = []

    def count_occurrences(number, lst):
        return lst.count(number)
    
    for line in lines:
        left, right = map(int, line.strip().split())
        left_side.append(left)
        right_side.append(right)

    total_score = 0
    for i in range(len(left_side)):
        total_score += count_occurrences(left_side[i], right_side) * left_side[i]

    return total_score

def main():
    lines = read_input_lines(1)
    
    part1_result = solve_part1(lines)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part2(lines)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()
