from pathlib import Path
from typing import List

def read_input(day: int) -> str:
    """Read the input file for the given day."""
    input_file = Path(__file__).parents[1] / 'inputs' / f'day{day:02d}.txt'
    return input_file.read_text().strip()

def read_input_lines(day: int) -> List[str]:
    """Read the input file for the given day and return it as a list of lines."""
    return read_input(day).split('\n')
