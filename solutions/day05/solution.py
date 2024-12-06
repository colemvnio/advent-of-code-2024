from utils.input_reader import read_input_lines
from typing import List, Tuple

# Get rules and updates from input
def parse_input(lines):
    rules = []
    updates = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Indicates a 'rule'
        if '|' in line:
            parts = line.split('|')
            if len(parts) != 2:
                continue
            try:
                # Extracts page numbers
                X, Y = int(parts[0].strip()), int(parts[1].strip())
                rules.append((X, Y))
            except:
                continue
        # Indicates an 'update'
        elif ',' in line:
            parts = line.split(',')
            try:
                update = [int(p.strip()) for p in parts if p.strip()]
                if update:
                    updates.append(update)
            except:
                continue
    return rules, updates

# Check if update follows all rules
def is_update_valid(update, rules):
    pos = { page: idx for idx, page in enumerate(update) }
    for X, Y in rules:
        if X in pos and Y in pos:
            if pos[X] >= pos[Y]:
                return False
    return True

def get_middle_page(update):
    return update[len(update) // 2]

# Idea: For each update, check if it follows the rules.
# If yes, add its middle page to the total.
def solve_part1(lines):
    rules, updates = parse_input(lines)
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            total += get_middle_page(update)
    return total

# Idea: Find wrong updates, fix their order using rules, then add their middle pages
def solve_part2(lines):
    rules, updates = parse_input(lines)
    total = 0
    invalid_updates = [u for u in updates if not is_update_valid(u, rules)]
    
    for update in invalid_updates:
        pages = set(update)
        adj = {}
        in_degree = {}
        
        for X, Y in rules:
            if X in pages and Y in pages:
                if X not in adj:
                    adj[X] = []
                adj[X].append(Y)
                in_degree[Y] = in_degree.get(Y, 0) + 1
        
        queue = [p for p in update if in_degree.get(p, 0) == 0]
        sorted_order = []
        
        while queue:
            current = queue.pop(0)
            sorted_order.append(current)
            for neighbor in adj.get(current, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(sorted_order) == len(update):
            total += get_middle_page(sorted_order)
    
    return total

def main():
    lines = read_input_lines(5)
    
    part1 = solve_part1(lines)
    print(f"Part 1: {part1}")
    
    part2 = solve_part2(lines)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
