from pacman import Pacman


field = [[Pacman.GHOST_FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD,
            Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.GHOST_FOOD],
        [Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.WALL,
            Pacman.WALL, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD],
        [Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD,
            Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD],
        [Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD,
            Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.FOOD],
        [Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD,
            Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD],
        [Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.WALL,
            Pacman.WALL, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.FOOD],
        [Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD,
            Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD],
        [Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.WALL,
            Pacman.WALL, Pacman.WALL, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.WALL, Pacman.WALL, Pacman.FOOD],
        [Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD,
            Pacman.PACMAN, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.WALL, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD, Pacman.FOOD]]

game = Pacman(field, 4)


game.play()
