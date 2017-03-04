# OOP Tic Tac Toe

For this project, we're going to apply our knowledge of OOP to design a simple Tic Tac Toe game. The final code is going to be rather simple, what's really important is to design it carefully. **Think about the design with your teammates** (you can try drawing, brainstorming, etc).

## Board

There are two big "parts" to solve in this project. The Board of the game is one of them. We've decided to build a dumb class as a board, that doesn't know much about the Tic Tac Toe game per se. It just has knowledge about its current state.

A `Board`, once initialized, will have a few handful methods like `get_row`, `get_column` and `get_diagonal`.

The tests for the board seem enough for you to understand it. For example, take a look at the [test_row](https://github.com/rmotr-group-projects/itp-w3-tic-tac-toe/blob/master/tests/test_board.py#L50) method. We just create a board, and we try to get the first row, which of course returns the elements on the first row of the board:

```python
board = Board([
    ['X', None, None],
    ['O', 'X', None],
    [None, 'O', 'X'],
])
row_0 = board.get_row(0)
print(row_0)  # ['X', None, None]

col_0 = board.get_column(0)
print(col_0)  # ['X', 'O', None]
```

**The most important** thing about the Board class, is how you design the interal data structure of your board. How are you going to store the elements of your board. That's going to have a profound impact in your end solution. Example: if you choose a list of lists (as the code above) or a dictionary:

```python
board_data_as_lists = [
    ['X', None, None],
    ['O', 'X', None],
    [None, 'O', 'X'],
]
board_data_as_dict = {
    0: ['X', None, None],
    1: ['O', 'X', None],
    2: [None, 'O', 'X'],
}
```

## Game

Now we get into the actual Tic Tac Toe game. The `Game` class is the one that contains all the **business logic** to play the game. The Board, for example, didn't know when there was a winner, because that's **business logic**. In Tic Tac Toe you have a winner if all the elements in a row are the same: again, that's **business logic**.

A `Game` will use a `Board` class to store all its data, and it'll add the business logic on top of it. A `Game` will be the main class the user interacts with. For example: whenever you want to make a _move_, you'll do `game.move(...)` that internally will invoke `board.move(...)`. The difference is that the `Game` class will add all the business logic to that move: check if the position is already taken, check if the game is already over, etc.

A game will also have a set of utility methods to check the state of the game: `is_finished()`, `has_winner()`, `get_winner()`, `is_tied()`. 
