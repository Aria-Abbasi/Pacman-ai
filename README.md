# Pacman Game

This is a simple implementation of the classic Pacman game in Python. The game is played on a grid, with Pacman, ghosts, food, and walls.

## Features

- Pacman and ghosts move around the grid.
- Pacman eats food to gain points.
- The game ends when all the food is eaten (win) or when a ghost catches Pacman (lose).

## How to Run

You can run the game by executing the `pacman.py` script with Python 3. Make sure you have the `matplotlib` library installed.

```bash
python3 pacman.py
```

## Game Rules

- Pacman starts at a specific position on the grid and can move up, down, left, or right.
- There are two ghosts that move randomly around the grid.
- Pacman gains points by eating food.
- The game ends when all the food is eaten or when a ghost catches Pacman.

## Implementation Details

The game is implemented using a simple grid system, where each cell in the grid can be empty, contain food, a wall, Pacman, or a ghost. The game uses the matplotlib library to visualize the game grid.

## Future Improvements

- Add more ghosts and different types of food.
- Implement different strategies for the ghosts to make the game more challenging.
- Improve the game visualization.