import itertools
import matplotlib.pyplot as plt
import copy
import math
import random


class Game:
    VALID_DIRECTIONS = ['u', 'd', 'l', 'r']
    NUMBER_OF_GHOSTS = 2
    PACMAN = 'P'
    EMPTY = ' '
    FOOD = '.'
    WALL = '|'
    GHOST_FOOD = 'GF'
    GHOST = 'G'

    def __init__(self, field):
        self.field = field
        self.score = 0
        self.won = None
        self.pacman_position = None
        self.ghost_positions = []
        self._initialize_positions()

    def _initialize_positions(self):
        for i, row in enumerate(self.field):
            for j, cell in enumerate(row):
                if cell == self.PACMAN:
                    self.pacman_position = (i, j)
                elif cell == self.GHOST or cell == self.GHOST_FOOD:
                    self.ghost_positions.append((i, j))


def initialize_game():
    field = [
        [Game.GHOST_FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD,
            Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.GHOST_FOOD],
        [Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.WALL,
            Game.WALL, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD],
        [Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD,
            Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD],
        [Game.FOOD, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD,
            Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.FOOD],
        [Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD,
            Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD],
        [Game.FOOD, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.WALL,
            Game.WALL, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.FOOD],
        [Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD,
            Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD],
        [Game.FOOD, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.WALL,
            Game.WALL, Game.WALL, Game.WALL, Game.FOOD, Game.WALL, Game.FOOD, Game.WALL, Game.WALL, Game.FOOD],
        [Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD,
            Game.PACMAN, Game.FOOD, Game.FOOD, Game.FOOD, Game.WALL, Game.FOOD, Game.FOOD, Game.FOOD, Game.FOOD]
    ]

    return Game(field)


def get_permutations(lst, n):
    return [p for p in itertools.product(lst, repeat=n)]


def print_ground(game):
    element_to_number = {
        Game.EMPTY: 0,
        Game.PACMAN: 1,
        Game.GHOST: 2,
        Game.FOOD: 3,
        Game.GHOST_FOOD: 2,
        Game.WALL: 8,
    }

    field = [[element_to_number[element]
              for element in row] for row in game.field]

    plt.imshow(field, cmap='Pastel1')
    plt.title(f'Score: {game.score}')
    plt.draw()
    plt.pause(0.001)

    # for row in game.field:
    #     print(' '.join(row))
    # print()


def win_or_lost_or_nothing(game):
    flat_ground = [item for sublist in game.field for item in sublist]

    food_count = flat_ground.count(Game.FOOD)
    food_count += flat_ground.count(Game.GHOST_FOOD)
    ghost_count = flat_ground.count(Game.GHOST)
    ghost_count += flat_ground.count(Game.GHOST_FOOD)
    pacman_count = flat_ground.count(Game.PACMAN)

    if food_count == 0:
        game.won = True
    elif ghost_count != Game.NUMBER_OF_GHOSTS or pacman_count != 1:
        game.won = False


def move_pacman(game, direction):
    pacman_position = game.pacman_position

    if pacman_position is None:
        return False

    new_position = get_new_position(pacman_position, direction)
    game.score -= 1

    if not is_valid_position(game, new_position):
        return False

    if game.field[new_position[0]][new_position[1]] == Game.FOOD:
        game.score += 10

    game.field[new_position[0]][new_position[1]] = Game.PACMAN
    game.field[pacman_position[0]][pacman_position[1]] = Game.EMPTY
    game.pacman_position = new_position

    return True


def move_ghosts(game, directions):
    for index, ghost_position in enumerate(game.ghost_positions):
        new_position = get_new_position(ghost_position, directions[index])

        if not is_valid_position(game, new_position):
            continue

        if game.field[ghost_position[0]][ghost_position[1]] == Game.GHOST_FOOD:
            game.field[ghost_position[0]][ghost_position[1]] = Game.FOOD
        else:
            game.field[ghost_position[0]][ghost_position[1]] = Game.EMPTY

        if game.field[new_position[0]][new_position[1]] == Game.FOOD:
            game.field[new_position[0]][new_position[1]] = Game.GHOST_FOOD
        else:
            game.field[new_position[0]][new_position[1]] = Game.GHOST

        game.ghost_positions.remove(ghost_position)
        game.ghost_positions.append(new_position)


def get_new_position(position, direction):
    x, y = position
    if direction == 'u':
        return x - 1, y
    elif direction == 'd':
        return x + 1, y
    elif direction == 'l':
        return x, y - 1
    elif direction == 'r':
        return x, y + 1
    else:
        return x, y


def is_valid_position(game, position):
    x, y = position
    if x < 0 or y < 0 or x >= len(game.field) or y >= len(game.field[0]):
        return False
    if game.field[x][y] == Game.WALL:
        return False
    return True


def move(game, direction, is_pacman):
    if is_pacman:
        move_pacman(game, direction)
    else:
        move_ghosts(game, direction)
    win_or_lost_or_nothing(game)
    return game


def len_shortest_path_to_food(game):
    x, y = game.pacman_position
    field = game.field
    queue = [(x, y, 0)]
    visited = set()
    while len(queue) > 0:
        x, y, distance = queue.pop(0)
        if field[x][y] == Game.FOOD:
            return distance
        if (x, y) not in visited:
            visited.add((x, y))
            if is_valid_position(game, (x - 1, y)):
                queue.append((x - 1, y, distance + 1))
            if is_valid_position(game, (x + 1, y)):
                queue.append((x + 1, y, distance + 1))
            if is_valid_position(game, (x, y - 1)):
                queue.append((x, y - 1, distance + 1))
            if is_valid_position(game, (x, y + 1)):
                queue.append((x, y + 1, distance + 1))
    return math.inf


def evaluate_game(game):
    if game.won:
        return math.inf
    elif game.won is not None:
        return -math.inf
    return game.score - len_shortest_path_to_food(game)


def minimax(game, depth, maximizingPlayer):
    if depth == 0 or game.won is not None:
        return evaluate_game(game), None

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        all_moves = {}
        for direction in Game.VALID_DIRECTIONS:
            new_game = move(copy.deepcopy(game), direction, True)
            if new_game is not None:
                eval, _ = minimax(new_game, depth - 1, False)
                all_moves[direction] = eval
                if eval > maxEval:
                    maxEval = eval
                    best_move = direction
        if depth == 4:
            print(all_moves)
        return maxEval, best_move
    else:
        minEval = float('inf')
        for directions in get_permutations(Game.VALID_DIRECTIONS, Game.NUMBER_OF_GHOSTS):
            new_game = move(copy.deepcopy(game), directions, False)
            if new_game is not None:
                eval, _ = minimax(new_game, depth - 1, True)
                if eval < minEval:
                    minEval = eval
        return minEval, None


def play():
    game = initialize_game()
    while game.won is None:
        print_ground(game)
        _, direction = minimax(game, 2, True)
        move(game, direction, is_pacman=True)
        directions = [random.choice(Game.VALID_DIRECTIONS)
                      for _ in range(Game.NUMBER_OF_GHOSTS)]
        move(game, directions, is_pacman=False)
        win_or_lost_or_nothing(game)
    if game.won == True:
        print("You won!")
    else:
        print("You lost!")


plt.ion()

play()
