from pathlib import Path
from typing import List

def read_input(day: int, test:bool = False) -> str:
    """Read the input file for the given day."""
    file_name = f'day{day:02d}-test.txt' if test else f'day{day:02d}.txt'
    input_file = Path(__file__).parents[1] / 'inputs' / file_name
    return input_file.read_text().strip()

def read_input_lines(day: int, test: bool = False) -> List[str]:
    """Read the input file for the given day and return it as a list of lines."""
    return read_input(day, test).split('\n')
