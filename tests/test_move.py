from board import Board, Coordinate, EMPTY, OTHER_SNAKE_HEAD, FOOD, MY_HEAD, MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT
from move import food_that_i_am_closest, moves_sorted_by_area_rank


def test_food_that_i_am_closest_without_other_snakes():
    # ####F
    # #M###
    # ###F#
    # #####
    # F###F
    board = Board(
        {
            Coordinate(0, 0): EMPTY,
            Coordinate(0, 1): EMPTY,
            Coordinate(0, 2): EMPTY,
            Coordinate(0, 3): EMPTY,
            Coordinate(0, 4): FOOD,
            Coordinate(1, 0): EMPTY,
            Coordinate(1, 1): MY_HEAD,
            Coordinate(1, 2): EMPTY,
            Coordinate(1, 3): EMPTY,
            Coordinate(1, 4): EMPTY,
            Coordinate(2, 0): EMPTY,
            Coordinate(2, 1): EMPTY,
            Coordinate(2, 2): EMPTY,
            Coordinate(2, 3): FOOD,
            Coordinate(2, 4): EMPTY,
            Coordinate(3, 0): EMPTY,
            Coordinate(3, 1): EMPTY,
            Coordinate(3, 2): EMPTY,
            Coordinate(3, 3): EMPTY,
            Coordinate(3, 4): EMPTY,
            Coordinate(4, 0): EMPTY,
            Coordinate(4, 1): FOOD,
            Coordinate(4, 2): EMPTY,
            Coordinate(4, 3): EMPTY,
            Coordinate(4, 4): FOOD,
        }
    )
    board._my_head = Coordinate(1, 1)

    result = food_that_i_am_closest(board, board.available_moves())
    assert result == MOVE_RIGHT


def test_food_that_i_am_closest_with_other_snakes():
    # ####F
    # #####
    # ###FM
    # ###S#
    # F###F
    board = Board(
        {
            Coordinate(0, 0): EMPTY,
            Coordinate(0, 1): EMPTY,
            Coordinate(0, 2): EMPTY,
            Coordinate(0, 3): EMPTY,
            Coordinate(0, 4): FOOD,
            Coordinate(1, 0): EMPTY,
            Coordinate(1, 1): EMPTY,
            Coordinate(1, 2): EMPTY,
            Coordinate(1, 3): EMPTY,
            Coordinate(1, 4): EMPTY,
            Coordinate(2, 0): EMPTY,
            Coordinate(2, 1): EMPTY,
            Coordinate(2, 2): EMPTY,
            Coordinate(2, 3): FOOD,
            Coordinate(2, 4): MY_HEAD,
            Coordinate(3, 0): EMPTY,
            Coordinate(3, 1): EMPTY,
            Coordinate(3, 2): EMPTY,
            Coordinate(3, 3): OTHER_SNAKE_HEAD,
            Coordinate(3, 4): EMPTY,
            Coordinate(4, 0): EMPTY,
            Coordinate(4, 1): FOOD,
            Coordinate(4, 2): EMPTY,
            Coordinate(4, 3): EMPTY,
            Coordinate(4, 4): FOOD,
        }
    )
    board._my_head = Coordinate(2, 4)

    result = food_that_i_am_closest(board, board.available_moves())
    assert result == MOVE_UP


def test_move_towards_best_value():
    # ##A##
    # SS#SS
    # #SM##
    # ##S##
    # #####
    board = Board(
        {
            Coordinate(0, 0): EMPTY,
            Coordinate(0, 1): OTHER_SNAKE_HEAD,
            Coordinate(0, 2): EMPTY,
            Coordinate(0, 3): EMPTY,
            Coordinate(0, 4): EMPTY,
            Coordinate(1, 0): EMPTY,
            Coordinate(1, 1): OTHER_SNAKE_HEAD,
            Coordinate(1, 2): OTHER_SNAKE_HEAD,
            Coordinate(1, 3): EMPTY,
            Coordinate(1, 4): EMPTY,
            Coordinate(2, 0): FOOD,
            Coordinate(2, 1): EMPTY,
            Coordinate(2, 2): MY_HEAD,
            Coordinate(2, 3): OTHER_SNAKE_HEAD,
            Coordinate(2, 4): EMPTY,
            Coordinate(3, 0): EMPTY,
            Coordinate(3, 1): OTHER_SNAKE_HEAD,
            Coordinate(3, 2): EMPTY,
            Coordinate(3, 3): EMPTY,
            Coordinate(3, 4): EMPTY,
            Coordinate(4, 0): EMPTY,
            Coordinate(4, 1): OTHER_SNAKE_HEAD,
            Coordinate(4, 2): EMPTY,
            Coordinate(4, 3): EMPTY,
            Coordinate(4, 4): EMPTY,
        }
    )
    board._my_head = Coordinate(2, 2)

    result = moves_sorted_by_area_rank(board, board.available_moves())
    assert result == [(MOVE_RIGHT, 12), (MOVE_UP, 6.5)]


def test_wants_to_move_towards_apple():
    # #####
    # #####
    # A#M##
    # #####
    # #####
    board = Board.from_height_and_width(5, 5)
    board._my_head = Coordinate(2, 2)
    board._board[Coordinate(0, 2)] = FOOD
    board._board[board.my_head] = MY_HEAD

    result = moves_sorted_by_area_rank(board, board.available_moves())
    assert result == [(MOVE_DOWN, 24.5), (MOVE_LEFT, 24.5), (MOVE_UP, 24.5), (MOVE_RIGHT, 24.5)]
