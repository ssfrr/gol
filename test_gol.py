import gol as g

def test_tick_empty_returns_empty():
    assert g.tick(set([])) == set([])

def test_tick_single_cell_dies():
    assert g.tick(set([(2,3)])) == set([])

def test_tick_four_cell_block_is_steady_state():
    square = set([(2,3), (3,3), (2,2), (3,2)])
    assert g.tick(square) == square

def test_get_neighbors_gives_all_neighbors():
    coords = (4,5)
    neighbors = set([(x,y) for x in range(3,6) for y in range(4,7)])
    neighbors.remove(coords)
    assert g.get_neighbors(coords) == neighbors

def test_get_border_gets_border_set():
    live_cells = set([(0,0), (1,0), (1,1)])
    border = set([(-1,0), (-1,1), (0, 1), (0, 2), (1, 2), (2,2), (2, 1),
        (2, 0), (2, -1), (1, -1), (0, -1), (-1, -1)])
    assert g.get_border(live_cells) == border

def test_vertical_line_becomes_horizontal_line():
    world_before = set([(0, -1), (0, 0), (0, 1)])
    world_after = set([(-1, 0), (0, 0), (1, 0)])
    assert g.tick(world_before) == world_after

def test_cell_with_no_neighbors_dies():
    cell = (4,5)
    lonely_world = set([cell])
    assert g.cell_survives(lonely_world, cell) is False

def test_cell_with_four_neighbors_dies():
    cell = (4,5)
    crowded_world = set([cell, (3,5), (4,4), (5,5), (3,4)])
    assert g.cell_survives(crowded_world, cell) is False

def test_cell_with_three_neighbors_survives():
    cell = (4,5)
    comfortable_world = set([cell, (3,5), (4,4), (5,5)])
    assert g.cell_survives(comfortable_world, cell) is True

def test_dead_cell_with_two_neighbors_stays_dead():
    cell = (4,5)
    lonely_world = set([cell, (3,5), (4,4)])
    assert g.cell_is_born(lonely_world, cell) is False

def test_dead_cell_with_three_neighbors_is_born():
    cell = (4,5)
    comfortable_world = set([cell, (3,5), (4,4), (5,5)])
    assert g.cell_is_born(comfortable_world, cell) is True
