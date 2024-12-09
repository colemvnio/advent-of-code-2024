from utils.input_reader import read_input_lines
import math

# Idea:
def solve_part1(lines):
    # Group antennas by frequency, with a list of coordinates as tuples
    freq_dict = {}
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell != ".":
                if cell not in freq_dict:
                    freq_dict[cell] = []
                freq_dict[cell].append((x, y))
    
    # Find all antinodes
    antinodes = set()
    max_y = len(lines)
    max_x = max(len(line) for line in lines) if lines else 0

    for freq, coords in freq_dict.items():
        if len(coords) < 2:
            continue
        
        for i in range (len(coords)):
            for j in range (i + 1, len(coords)):
                x1, y1 = coords[i]
                x2, y2 = coords[j]

                dx = x1 - x2
                dy = y1 - y2

                distance = math.hypot(dx, dy)
                if distance == 0:
                    continue # Skip due to same position

                # Vector requirements
                ux = dx / distance
                uy = dy / distance

                ax1 = x1 - 2 * dx
                ay1 = y1 - 2 * dy

                ax2 = x2 + 2 * dx
                ay2 = y2 + 2 * dy

                antinode1 = (round(ax1), round(ay1))
                antinode2 = (round(ax2), round(ay2))

                # Check bounds
                if 0 <= antinode1[0] < max_x and 0 <= antinode1[1] < max_y:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < max_x and 0 <= antinode2[1] < max_y:
                    antinodes.add(antinode2)
                   
    return len(antinodes)

# Idea: 
def solve_part2(lines):
    total = 0
    return total


def main():
    lines = read_input_lines(8)
    
    part1 = solve_part1(lines)
    print(f"Part 1: {part1}")
    
    part2 = solve_part2(lines)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
