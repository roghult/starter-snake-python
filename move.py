import random
from typing import Optional

from board import Board, Coordinate

MOVE_UP = "up"
MOVE_DOWN = "down"
MOVE_LEFT = "left"
MOVE_RIGHT = "right"
ALL_MOVES = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]


def determine_move(board: Board) -> str:
    closest_food_coordinate = food_that_i_am_closest(board)
    if closest_food_coordinate is None:
        move_in_direction = random_move_without_collision(board)
    else:
        move_in_direction = closest_food_coordinate
    return move_in_direction


def random_move_without_collision(board):
    # find coordinates I actually can move to
    available_moves = [move for move in ALL_MOVES if board.can_move_in_direction(move)]
    return random.choice(available_moves)


def food_that_i_am_closest(board: Board) -> Optional[Coordinate]:
    sorted_food_coordinate_and_distance = sorted([
        (food_coord, board.my_head.distance(food_coord)) for food_coord in board.food_coordinates
    ], key=lambda e: e[1])

    for food_coordinate, distance in sorted_food_coordinate_and_distance:
        opponent_distances = [each.distance(food_coordinate) for each in board.opponent_heads]
        if all(each > distance for each in opponent_distances):
            return food_coordinate

    return None
