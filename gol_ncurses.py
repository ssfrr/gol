import gol as g
import curses as c
import random
import time

def main():
    world = init_world()
    stdscr = c.initscr()
    max_x = stdscr.getmaxyx()[1]
    max_y = stdscr.getmaxyx()[0]

    try:
        c.noecho()
        c.curs_set(0)
        while(1):
            stdscr.erase()
            for cell in world:
                if cell[0] >= 0 and cell[1] >= 0 and \
                        cell[0] < max_x and cell[1] < max_y:
                    stdscr.addch(cell[1], cell[0], '*')
            stdscr.refresh()
            world = g.tick(world)
            time.sleep(0.1)

    finally:
        c.echo()
        c.curs_set(1)
        c.endwin()

def draw_char(screen, char, x, y):
    screen.addch(y, x, char)

def init_world():
    world = set([])
    for _ in range(30):
        world.add((random.randrange(40,60), random.randrange(10,20)))
    return world

if __name__ == "__main__":
    main()
