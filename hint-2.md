# Hint 2 - Move logic

The `move` method of the game class is probably one of the most important methods for this game. But this method, is rather simple if you have figured out all the other utility methods: `is_finished()`, `has_winner()`, `get_winner()`, `is_tied()`. 

Then, `move()`, is just a matter of checking if any of those methods already is True. For example, if you try to make a move, but `is_finished()` returns `True`, then that shouldn't be a valid move.

```python
# pseudocode, not actual code.
def move():
    if player != next_player:
        raise exception
    if row not valid position:  # valid positions [0, 1, 2]
        raise exception
    if col not in valid position:
        raise exception
    if position_is_already_taken:
        raise exception
    if self.is_finished():
        raise exception
        
    # All good, make the move!
    self.board.move(player, row, col)
    self.next_player = 'X' if player == 'O' else 'O'
```

## Is finished?

Is finished is also another method that relies on the utility methods:

```python
# pseudocode, not actual code.
def is_finished():
    if has_winner() or is_tied():
        return True
    return False
```

## Has Winner?

Has winner can just use the `get_winner()` method:

```python
# pseudocode, not actual code.
def has_winner():
    if get_winner() is not None:
        return True
    return False
```
