import pygame as pg
from random import randint

WIDTH, HEIGHT = (1000, 800)
FPS = 30
CELL_SIZE = 8
CELL_BORDER = 1
EMPTY_CELL_COLOR = (40, 40, 40)
ALIVE_CELL_COLOR = (150, 150, 150)
BACKGROUND_COLOR = (30, 30, 30)
GRID_SIZE = 100

class GameLogic:
    def __init__(self) -> None:
        pg.init()
        self.Window = pg.display.set_mode((WIDTH, HEIGHT))
        self.Clock = pg.time.Clock()
        self.running = True
        self.grid = [[randint(0, 1)] * GRID_SIZE for _ in range(GRID_SIZE)]
        

    def draw_window(self) -> None:
        self.Window.fill(BACKGROUND_COLOR) #BG color
        for x in range(GRID_SIZE): 
            for y in range(GRID_SIZE):
                pg.draw.rect(self.Window, ALIVE_CELL_COLOR if self.grid[x][y] else EMPTY_CELL_COLOR, (x*CELL_SIZE + CELL_BORDER, y*CELL_SIZE + CELL_BORDER, CELL_SIZE - CELL_BORDER, CELL_SIZE - CELL_BORDER))

        pg.display.flip()

    def handle_events(self) -> None:
        #button Just Pressed (and events)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.stop()
            if event.type != pg.KEYDOWN:
                continue
            if event.key == pg.K_ESCAPE:
                self.stop()

    def handle_input(self) -> None:
        if not pg.key.get_focused():
            return
        #button Held
        keys = pg.key.get_pressed()
        ...

    def cell_get_neighbors(self, cell: tuple[int, int]) -> int:
        neighbors_count: int = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # Maybe make it global
        x, y = cell
        for cd, rd in directions:
            if (0 < x + cd < GRID_SIZE) and (0 < y + rd < GRID_SIZE):
                if self.grid[x+cd][y+rd]:
                    neighbors_count += 1
        
        return neighbors_count

    def cells_logic(self) -> None:
        # Optimisation: Put all alive cells in dictionary
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                neighbors = self.cell_get_neighbors((x, y))
                if self.grid[x][y] == 0 and neighbors == 3:
                    self.grid[x][y] = 1
                elif self.grid[x][y] == 1 and (neighbors < 2 or neighbors > 3):
                    self.grid[x][y] = 0
    
    def update(self) -> None:
        while self.running:
            self.handle_events()
            self.handle_input()
            self.cells_logic()
            self.draw_window()
            self.dt = self.Clock.tick(FPS) * 0.001
        pg.quit()

    def stop(self) -> None:
        self.running = False

if __name__ == "__main__":
    GameInstance = GameLogic()
    GameInstance.update()