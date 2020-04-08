from board import Board, Coordinate, EMPTY, OTHER_SNAKE_HEAD, FOOD, MY_HEAD, MOVE_UP, MOVE_DOWN
from move import food_that_i_am_closest


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

    result = food_that_i_am_closest(board)
    assert result == MOVE_DOWN


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

    result = food_that_i_am_closest(board)
    assert result == MOVE_UP
