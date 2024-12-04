from utils.input_reader import read_input_lines

# Idea: Allow grid analysis to identify a word in any direction without performing brute force
def solve_part1(lines: list[str]) -> int:
    word_count = 0
    word = "XMAS"

    # Direction vectors: up, down, left, right, up-right, up-left, down-right, down-left
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def check_word(current_grid, x, y, dx, dy):
        # Early exit
        if current_grid[x][y] != word[0]:
            return False

        word_found = True
        rows, cols = len(current_grid), len(current_grid[0])
        
        for i in range(len(word)):
            new_x = x + dx * i
            new_y = y + dy * i

            # Checks if the word is out of bounds, causing an early return/exit
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                word_found = False
                break

            # Checks if there's an unrelated character, causing an early return/exit
            if current_grid[new_x][new_y] != word[i]:
                word_found = False
                break

        return word_found
    
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            # Early exit
            if lines[x][y] != word[0]:
                continue

            for dx, dy in directions:
                if check_word(lines, x, y, dx, dy):
                    word_count += 1

    return word_count


# Idea: Construct diagonal lines from corner to corner, forming an "X" shape.
# Analyze this "X" pattern by excluding invalid sequences, and confirming if the word is present
def solve_part2(lines: list[str]) -> int:
    word_count = 0
    word = "MAS"
    triggering_letter = "A" # Middle letter acting as an indicator to perform the search

    diagonal_pairs = [
        ((1, 1), (-1, -1)),  # Orientation: \
        ((1, -1), (-1, 1))   # Orientation: /
    ]

    def check_word(current_grid, x, y):
        rows, cols = len(current_grid), len(current_grid[0])
        
        # Evaluate a full X pattern
        for pair in diagonal_pairs:
            # Get the complete "line" from tip to tip
            x1, y1 = x + pair[0][0], y + pair[0][1]
            x2, y2 = x + pair[1][0], y + pair[1][1]
            
            # Checks if the word is out of bounds, causing an early return/exit
            if not (0 <= x1 < rows and 0 <= y1 < cols and
                    0 <= x2 < rows and 0 <= y2 < cols):
                return False
            
            # Checks if there's an unrelated character/invalid pattern, causing an early return/exit
            if not ((current_grid[x1][y1] == word[0] and current_grid[x2][y2] == word[2]) or
                    (current_grid[x1][y1] == word[2] and current_grid[x2][y2] == word[0])):
                return False
        
        return True

    for x in range(len(lines)):
        for y in range(len(lines[0])):
            # Early exit for evaluation/algo simplification
            if lines[x][y] != triggering_letter:
                continue
            
            word_count += check_word(lines, x, y)

    return word_count

def main():
    lines = read_input_lines(4)
    
    part1_result = solve_part1(lines)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part2(lines)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()
