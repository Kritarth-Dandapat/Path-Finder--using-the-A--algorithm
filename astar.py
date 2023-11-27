
import pygame
from queue import PriorityQueue
from algorithm import algorithm
from pixels import Spot

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Visualized")


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def make_grid(rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
                grid.append([])
                for j in range(rows):
                        spot = Spot(i, j , gap, rows)
                        grid[i].append(spot)
        return grid

def draw_grid(win, rows, width):
        gap = width // rows
        for i in range(rows):
                pygame.draw.line(win, GREY, (0,i * gap), (width, i * gap))
                for j in range(rows):
                        pygame.draw.line(win, GREY, (j * gap, 0), ( j * gap, width))
                

def draw(win, grid, rows, width):
        win.fill(WHITE)

        for row in grid:
                for spot in row:
                        spot.draw(win)
        
        draw_grid(win, rows, width)
        pygame.display.update()

def get_clicked_position(pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y//gap
        col = x // gap

        return row, col

def main(win, width):
        ROWS = 50
        grid = make_grid(ROWS, width)

        start = None
        end = None

        run = True
        started = False

        while run:
                draw(win, grid, ROWS, width)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False

                        if pygame.mouse.get_pressed()[0]: # left mouse button
                                pos = pygame.mouse.get_pos()
                                x, y = get_clicked_position(pos, ROWS, width)
                                spot = grid[x][y]

                                if not start and spot != end:
                                        start = spot
                                        start.make_start()
                                elif not end and spot != start:
                                        end = spot
                                        end.make_end()
                                elif spot != end and spot != start:
                                        spot.make_barrier()


                        elif pygame.mouse.get_pressed()[2]:# right mouse button
                                pos = pygame.mouse.get_pos()
                                row, col = get_clicked_position(pos, ROWS, width)
                                spot = grid[row][col]
                                spot.reset()
                                if spot == start:
                                        start = None
                                elif spot == end:
                                        end = None
                        
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE and start and end:
                                        for row in grid:
                                                for spot in row:
                                                        spot.update_neighbours(grid)
                                        algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end)
                                
                                if event.key == pygame.K_c:
                                        start = None
                                        end = None
                                        grid = make_grid(ROWS, width)

        pygame.quit()

main(WIN, WIDTH)



                       
                        
                