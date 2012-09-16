def tick(world):
    '''
    Given a set of cells representing all living cells in the world,
    computes the next set of living cells based on the rules of
    Conway's Game of Life.
    '''
    # Find all cells that stay alive from the current alive set
    next_world = set([cell for cell in world
        if cell_survives(world, cell)])
    # Now find all cells that are newly born from the set of
    # border cells
    next_world |= set([cell for cell in get_border(world)
        if cell_is_born(world, cell)])
    return next_world

def get_neighbors(cell):
    '''
    Returns a list of all 8 cells adjacent to a given cell.
    '''
    neighbors = set([(cell[0] - x, cell[1] - y)
        for x in range(-1,2)
        for y in range(-1,2)])
    neighbors.remove(cell)
    return neighbors

def get_border(cells):
    '''
    Returns a list of all cells that are not in the given cell set
    but are adjacent to cells in it.
    '''
    border = set([])
    for cell in cells:
        border |= get_neighbors(cell)
    return border - cells

def cell_survives(world, cell):
    '''
    Returns True if the given cell will survive in the given world.
    Undefined behavior if the cell is not already alive in the world.
    '''
    living_neighbors = get_neighbors(cell) & world
    return len(living_neighbors) == 2 or len(living_neighbors) == 3

def cell_is_born(world, cell):
    living_neighbors = get_neighbors(cell) & world
    return len(living_neighbors) == 3
