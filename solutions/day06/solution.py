from utils.input_reader import read_input_lines
from typing import List, Tuple

# Note: Index([0-99], [0-99]) based navigation
def find_initial_position(lines: List[str]) -> Tuple[int, int]:
    grid = [list(row) for row in lines]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return (x, y)
    # Failsafe, shouldn't reach this                
    return (-1, -1)

def is_in_bounds(x: int, y: int, grid: List[List[str]]) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def navigate(x: int, y: int, direction: str, grid: List[List[str]]) -> Tuple[int, int]:
    if direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'U':
        y -= 1
    elif direction == 'D':
        y += 1
    return (x, y)

def turn_right(current_direction: str) -> str:
    if current_direction == 'R':
        return 'D'
    elif current_direction == 'L':
        return 'U'
    elif current_direction == 'U':
        return 'R'
    elif current_direction == 'D':
        return 'L'

def check_front(x: int, y: int, direction: str, grid: List[List[str]]) -> bool:
    next_x, next_y = navigate(x, y, direction, grid)
    return is_in_bounds(next_x, next_y, grid) and grid[next_y][next_x] != '#'

def print_path(grid: List[List[str]], visited: set):
    path_grid = [row[:] for row in grid]
    for x, y in visited:
        if path_grid[y][x] != '#':
            path_grid[y][x] = 'X'

# Idea: Navigate input grid, following the path while turning right when blocked, until reaching the edge/oob
def solve_part1(lines):
    grid = [list(row) for row in lines]
    x, y = find_initial_position(lines)
    visited = {(x, y)}
    current_direction = 'U' # Assumption
    
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 4 # Maximum number of steps based on input grid, failsafe
    
    print(f"Grid size: {len(grid[0])}x{len(grid)}")
    print(f"Starting at ({x}, {y}) facing {current_direction}")
    
    while True:
        # Always check end condition at every iteration before moving further
        if x == 0 or x == len(grid[0])-1 or y == 0 or y == len(grid)-1:
            # If we're facing outward, we're done
            next_x, next_y = navigate(x, y, current_direction, grid)
            if not is_in_bounds(next_x, next_y, grid):
                print(f"Reached edge, finished")
                break
        
        if not check_front(x, y, current_direction, grid):
            print(f"Blocked, turning right.")
            current_direction = turn_right(current_direction)
        else:
            next_x, next_y = navigate(x, y, current_direction, grid)
            if not is_in_bounds(next_x, next_y, grid):
                print(f"Preventing out of bounds")
                break
                
            print(f"Moving freely")
            x, y = next_x, next_y
            visited.add((x, y))
        
        steps += 1
        if steps > max_steps:
            print("Exceeded maximum steps, stopping")
            break
    
    return len(visited)

# Idea: 
def solve_part2(lines):
    total = 0
    
    return total

def main():
    lines = read_input_lines(6)
    
    part1 = solve_part1(lines)
    print(f"Part 1: {part1}")
    
    part2 = solve_part2(lines)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
