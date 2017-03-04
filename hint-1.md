# Hint 1 - Board elements

If you chose a list of lists to represent your board, getting rows, columns and diagonals should be simple.

Example:


```python
board_data_as_lists = [
    ['X', None, None],
    ['O', 'X', None],
    [None, 'O', 'X'],
]

def get_row(number):
    return board_data_as_lists[number] # Simple
    
def get_column(number):
    column = []
    for row in board_data_as_lists:
        column.append(row[number])

def get_diagonal(number):
    if number == 0:
        positions = [
            (0, 0),
            (1, 1),
            (2, 2),
        ]
    elif number == 1:
        positions = [
            (0, 2),
            (1, 1),
            (2, 0),
        ]
        
    diagonal = []
    for position in positions:
        row = position[0]
        col = position[1]
        diagonal.append(board_data_as_lists[row][col])

    return diagonal
```
