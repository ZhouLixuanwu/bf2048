from grid import Grid
from game_panel import GamePanel
from game import Game


if __name__ == '__main__':
    size = 4
    grid = Grid(size)
    panel = GamePanel(grid)
    game2048 = Game(grid, panel)
    game2048.start()

