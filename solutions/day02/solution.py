from utils.input_reader import read_input_lines

# Idea: Establish if the list is either increasing or decreasing
# by checking if the difference between each number is 1 and 3
# then count the number of safe reports
def solve_part1(lines: list[str]) -> int:
    safe_reports = 0
    
    def all_increasing(list):
        for i in range(len(list) - 1):
            curr_level = list[i]
            next_level = list[i + 1]
            
            # Check for increase, then for increase between bounds
            if next_level <= curr_level or abs(next_level - curr_level) > 3 or abs(next_level - curr_level) < 1:
                return False
        return True
    
    def all_decreasing(list):
        for i in range(len(list) - 1):
            curr_level = list[i]
            next_level = list[i + 1]
            
            # Check for decrease, then for decrease between bounds
            if next_level >= curr_level or abs(next_level - curr_level) > 3 or abs(next_level - curr_level) < 1:
                return False
        return True
    
    for line in lines:
        levels = list(map(int, line.strip().split()))
        if all_increasing(levels) or all_decreasing(levels):
            safe_reports += 1
    
    return safe_reports

# Idea: Applying the same logic as part 1, but with a problem dampener to establish if removing one element at a time a level could become safe
def solve_part2(lines: list[str]) -> int:
    safe_reports = 0

    def all_increasing(list):
        for i in range(len(list) - 1):
            curr_level = list[i]
            next_level = list[i + 1]
            
            # Check for increase, then for increase between bounds
            if next_level <= curr_level or abs(next_level - curr_level) > 3 or abs(next_level - curr_level) < 1:
                return False
        return True
    
    def all_decreasing(list):
        for i in range(len(list) - 1):
            curr_level = list[i]
            next_level = list[i + 1]
            
            # Check for decrease, then for decrease between bounds
            if next_level >= curr_level or abs(next_level - curr_level) > 3 or abs(next_level - curr_level) < 1:
                return False
        return True
    
    # Idea: Create test list by removing one element at a time and check if it is increasing or decreasing
    def problem_dampener(levels):
        for i in range(len(levels)):
            test_levels = levels[:i] + levels[i+1:]
            if all_increasing(test_levels) or all_decreasing(test_levels):
                return True
        return False
    
    for line in lines:
        levels = list(map(int, line.strip().split()))
        if (all_increasing(levels) or all_decreasing(levels)) or problem_dampener(levels):
            safe_reports += 1

    return safe_reports

def main():
    lines = read_input_lines(2)
    
    part1_result = solve_part1(lines)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part2(lines)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()
