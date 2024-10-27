import re

# Define the valid symbols (anything that isn't a period or a digit)
def is_symbol(char):
    return not char.isdigit() and char != '.'

# Read the schematic from the file
with open('text.txt', 'r') as file:
    schematic = [line.strip() for line in file.readlines()]

# Get the dimensions of the schematic
rows = len(schematic)
cols = len(schematic[0])

# Function to find adjacent cells (including diagonals)
def get_adjacent_indices(row, col, num_length):
    # Get all possible adjacent indices for the full length of a multi-digit number
    directions = [(-1, -1), (-1, 0), (-1, 1),  # Top row
                  (0, -1),         (0, 1),     # Left and right
                  (1, -1), (1, 0), (1, 1)]     # Bottom row
    adjacent = set()  # Use set to avoid duplicate positions
    for offset in range(num_length):
        for dr, dc in directions:
            adj_row = row
            adj_col = col + offset
            r, c = adj_row + dr, adj_col + dc
            if 0 <= r < rows and 0 <= c < cols:
                adjacent.add((r, c))
    return adjacent

# Initialize sum of part numbers
part_sum = 0

# Iterate through the schematic grid row by row
for row in range(rows):
    # Use regex to find all numbers in the row
    for match in re.finditer(r'\d+', schematic[row]):
        # Extract the number and its position
        num = int(match.group())
        col = match.start()
        num_length = len(match.group())

        # Check if adjacent to any symbol
        if any(is_symbol(schematic[r][c]) for r, c in get_adjacent_indices(row, col, num_length)):
            # Add to part sum if adjacent to a symbol
            part_sum += num

# Output the total sum of part numbers
print(part_sum)
