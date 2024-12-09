from utils.input_reader import read_input_lines

# Behaviour: 
# - Takes a string representing the disk map
# - Even indices represent file sizes
# - Odd indices represent free space sizes
# - Returns a list where:
#   - Files are represented by sequential IDs (0, 1, 2, etc.)
#   - Empty spaces are represented by "."
def parse_disk(disk):
    parsed = []
    file_id = 0
    i = 0

    while i < len(disk):
        size = int(disk[i])
        if i % 2 == 0:
            # Even index: File block
            parsed.extend([file_id] * size)
            file_id += 1
        elif i % 2 == 1:
            # Odd index: Free space
            parsed.extend(["."] * size)
        i += 1
    return parsed

# Behaviour:
# - Receives the parsed disk (e.g., [0,0,'.', '.', 1,1,1])
# - Redistributes (compacts) the disk by moving one file block at a time
#   from the end to the leftmost free space
def compact_disk(parsed_disk):
    step = 0  # To track the number of moves
    while True:
        # Goal: Move one file block from the end to the leftmost free space
        try:
            free_index = parsed_disk.index('.')
        except ValueError:
            break

        # Goal: Find the rightmost file block to the right of the free space
        move_index = -1
        for i in range(len(parsed_disk)-1, free_index, -1):
            if parsed_disk[i] != '.':
                move_index = i
                break

        if move_index == -1:
            break

        # Goal: Move the file block to the free space
        parsed_disk[free_index] = parsed_disk[move_index]
        parsed_disk[move_index] = '.'
        step += 1

    return parsed_disk

# Behaviour:
# - Calculates the filesystem checksum by summing (position * file_id) for each file block
def calculate_checksum(parsed_disk):
    checksum = 0
    for index, block in enumerate(parsed_disk):
        if block != ".":
            checksum += index * block
    return checksum

def solve_part1(lines):
    disk = lines[0].strip()
    parsed = parse_disk(disk)
    compacted_disk = compact_disk(parsed.copy())
    
    checksum = calculate_checksum(compacted_disk)
    return checksum

def solve_part2(lines):
    checksum = 0
    return checksum

def main():
    lines = read_input_lines(9)
    
    part1 = solve_part1(lines)
    print(f"\nPart 1: {part1}")
    
    part2 = solve_part2(lines)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
