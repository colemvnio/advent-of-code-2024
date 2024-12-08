from utils.input_reader import read_input_lines

def apply_operators(numbers, expected_value, operators=['+', '*', '||']):
    def evaluate(ops):
        result = numbers[0]
        for index, op in enumerate(ops):
            if op == '||':
                result = int(str(result) + str(numbers[index + 1]))
            elif op == '+':
                result += numbers[index + 1]
            elif op == '*':
                result *= numbers[index + 1]
        return result

    def generate_ops(n):
        if n == 0:
            yield []
        else:
            for op in operators:
                for sub_ops in generate_ops(n - 1):
                    yield [op] + sub_ops

    for ops in generate_ops(len(numbers) - 1):
        try:
            if evaluate(ops) == expected_value:
                return True
        except:
            continue
    return False

# Idea: Generate and apply all possible operator combinations
def solve_part1(lines):
    sum = 0

    for line in lines:
        expected_value = int(line.split(": ")[0])
        numbers = [int(x) for x in line.split(": ")[1].split(" ")]

        if apply_operators(numbers, expected_value, ['+', '*']):
            sum += expected_value

    return sum

# Idea: Generate and apply all possible operator combinations
def solve_part2(lines):
    total = 0

    for line in lines:
        expected_value = int(line.split(": ")[0])
        numbers = [int(x) for x in line.split(": ")[1].split(" ")]

        if apply_operators(numbers, expected_value, ['+', '*', '||']):
            total += expected_value

    return total


def main():
    lines = read_input_lines(7)
    
    part1 = solve_part1(lines)
    print(f"Part 1: {part1}")
    
    part2 = solve_part2(lines)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()
