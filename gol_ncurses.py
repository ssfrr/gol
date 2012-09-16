def main():
    stdscr = c.initscr()
    try:
        c.noecho()
        c.curs_set(0)
        while(1):
            for x in range(10,50):
                for y in range(10,30):
                    draw_char(stdscr, random.choice("* "), x, y)
            stdscr.refresh()

    finally:
        c.echo()
        c.curs_set(1)
        c.endwin()

def draw_char(screen, char, x, y):
    screen.addch(y, x, char)

if __name__ == "__main__":
    main()
