import itertools
import matplotlib.pyplot as plt
import copy
import random


def get_permutations(lst, n):
    return [p for p in itertools.product(lst, repeat=n)]


class Pacman:
    VALID_DIRECTIONS = ['u', 'd', 'l', 'r']
    DIRECTION_MAP = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }
    PACMAN = 'P'
    EMPTY = ' '
    FOOD = '.'
    WALL = '|'
    GHOST_FOOD = 'GF'
    GHOST = 'G'
    FOOD_REWARD = 10
    MOVE_PENALTY = 1
    ELEMENT_TO_NUMBER = {
        EMPTY: 0,
        PACMAN: 1,
        GHOST: 2,
        FOOD: 3,
        GHOST_FOOD: 2,
        WALL: 8,
    }

    def __init__(self, field, depth):
        plt.ion()
        self.field = field
        self.score = 0
        self.won = None
        self.pacman_position = None
        self.ghost_positions = []
        self.depth = depth
        self._initialize_positions()

    def _initialize_positions(self):
        for i, row in enumerate(self.field):
            for j, cell in enumerate(row):
                if cell == self.PACMAN:
                    self.pacman_position = (i, j)
                elif cell == self.GHOST or cell == self.GHOST_FOOD:
                    self.ghost_positions.append((i, j))

    def print_ground(self):
        field = [[self.ELEMENT_TO_NUMBER[element]
                  for element in row] for row in self.field]

        plt.imshow(field, cmap='Pastel1')
        plt.title(f'Score: {self.score}')
        plt.draw()
        plt.pause(0.0001)

    def check_endgame(self):
        flat_ground = [item for sublist in self.field for item in sublist]

        food_count = flat_ground.count(Pacman.FOOD)
        food_count += flat_ground.count(Pacman.GHOST_FOOD)
        ghost_count = flat_ground.count(Pacman.GHOST)
        ghost_count += flat_ground.count(Pacman.GHOST_FOOD)
        pacman_count = flat_ground.count(Pacman.PACMAN)

        if food_count == 0:
            self.won = True
        elif ghost_count != len(self.ghost_positions) or pacman_count != 1:
            self.won = False

    def move_pacman(self, direction):
        if self.pacman_position is None:
            return False

        new_position = self.get_new_position(self.pacman_position, direction)
        self.score -= Pacman.MOVE_PENALTY

        if not self.is_valid_position(new_position):
            return False

        new_cell = self.field[new_position[0]][new_position[1]]
        if new_cell == Pacman.FOOD:
            self.score += Pacman.FOOD_REWARD

        self.field[self.pacman_position[0]
                   ][self.pacman_position[1]] = Pacman.EMPTY
        self.field[new_position[0]][new_position[1]] = Pacman.PACMAN
        self.pacman_position = new_position

        return True

    def move_ghosts(self, directions):
        new_ghost_positions = []
        for index, ghost_position in enumerate(self.ghost_positions):
            new_position = self.get_new_position(
                ghost_position, directions[index])

            if not self.is_valid_position(new_position):
                new_ghost_positions.append(ghost_position)
                continue

            current_ghost_cell = self.field[ghost_position[0]
                                            ][ghost_position[1]]
            new_cell = self.field[new_position[0]][new_position[1]]

            if new_cell in [Pacman.GHOST, Pacman.GHOST_FOOD]:
                new_ghost_positions.append(ghost_position)
                continue

            self.field[ghost_position[0]][ghost_position[1]
                                          ] = Pacman.FOOD if current_ghost_cell == Pacman.GHOST_FOOD else Pacman.EMPTY
            self.field[new_position[0]][new_position[1]
                                        ] = Pacman.GHOST_FOOD if new_cell == Pacman.FOOD else Pacman.GHOST

            new_ghost_positions.append(new_position)

        self.ghost_positions = new_ghost_positions

    def get_new_position(self, position, direction):
        dx, dy = Pacman.DIRECTION_MAP.get(direction, (0, 0))
        x, y = position
        return x + dx, y + dy

    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < len(self.field) and 0 <= y < len(self.field[0]) and self.field[x][y] != Pacman.WALL

    def move(self, direction, is_pacman_turn):
        self.move_pacman(
            direction) if is_pacman_turn else self.move_ghosts(direction)
        self.check_endgame()
        return self

    def len_shortest_path_to_food(self, x=None, y=None):
        if x is None or y is None:
            x, y = self.pacman_position
        field = self.field
        queue = [(x, y, 0)]
        visited = set()
        while queue:
            x, y, distance = queue.pop(0)
            if field[x][y] == Pacman.FOOD and distance > 0:
                return distance
            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in self.DIRECTION_MAP.values():
                    new_position = (x + dx, y + dy)
                    if self.is_valid_position(new_position):
                        queue.append((*new_position, distance + 1))

        return len(field) * len(field[0])

    def neighbors_have_food_or_pacman(self, x, y):
        field = self.field
        if self.is_valid_position((x - 1, y)) and field[x - 1][y] in [Pacman.FOOD, Pacman.PACMAN]:
            return True
        if self.is_valid_position((x + 1, y)) and field[x + 1][y] in [Pacman.FOOD, Pacman.PACMAN]:
            return True
        if self.is_valid_position((x, y - 1)) and field[x][y - 1] in [Pacman.FOOD, Pacman.PACMAN]:
            return True
        if self.is_valid_position((x, y + 1)) and field[x][y + 1] in [Pacman.FOOD, Pacman.PACMAN]:
            return True
        return False

    def penalty_single_foods(self):
        field = self.field
        penalty = 0
        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == Pacman.FOOD and not self.neighbors_have_food_or_pacman(i, j):
                    penalty += self.len_shortest_path_to_food(i, j) + 10
        return penalty

    def evaluate_game(self):
        if self.won:
            return 100 * self.score
        elif self.won is not None:
            return float('-inf')
        return self.score - self.len_shortest_path_to_food() - self.penalty_single_foods()

    def minimax(self, depth, alpha, beta, is_pacman_turn):
        if depth == 0 or self.won is not None:
            return self.evaluate_game(), None

        if is_pacman_turn:
            maxEval = float('-inf')
            best_moves = []
            all_moves = {}
            for direction in Pacman.VALID_DIRECTIONS:
                new_game = copy.deepcopy(self)
                new_game.move(direction, is_pacman_turn=True)
                if new_game is not None:
                    eval, _ = new_game.minimax(
                        depth - 1, alpha, beta, is_pacman_turn=False)
                    all_moves[direction] = eval
                    if eval > maxEval:
                        maxEval = eval
                        best_moves = [direction]
                    elif eval == maxEval:
                        best_moves.append(direction)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            if depth == 4:
                print(all_moves)
            return maxEval, random.choice(best_moves) if best_moves else None
        else:
            minEval = float('inf')
            for directions in get_permutations(Pacman.VALID_DIRECTIONS, len(self.ghost_positions)):
                new_game = copy.deepcopy(self)
                new_game.move(directions, is_pacman_turn=False)
                if new_game is not None:
                    eval, _ = new_game.minimax(
                        depth - 1, alpha, beta, is_pacman_turn=True)
                    if eval < minEval:
                        minEval = eval
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return minEval, None

    def play(self):
        while self.won is None:
            self.print_ground()
            _, direction = self.minimax(self.depth, float(
                '-inf'), float('inf'), is_pacman_turn=True)
            self.move(direction, is_pacman_turn=True)
            directions = [random.choice(Pacman.VALID_DIRECTIONS)
                          for _ in range(len(self.ghost_positions))]
            self.move(directions, is_pacman_turn=False)
            self.check_endgame()
        if self.won == True:
            print("You won!")
        else:
            print("You lost!")
