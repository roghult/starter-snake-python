from typing import Optional

from board import Board, Coordinate

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


def move(board_data):
    pass


def avoid_collision():
    pass


def food_that_i_am_closest(board: Board) -> Optional[Coordinate]:
    sorted_food_coordinate_and_distance = sorted([
        (food_coord, board.my_head.distance(food_coord)) for food_coord in board.food_coordinates
    ], key=lambda e: e[1])

    for food_coordinate, distance in sorted_food_coordinate_and_distance:
        opponent_distances = [each.distance(food_coordinate) for each in board.opponent_heads]
        if all(each > distance for each in opponent_distances):
            return food_coordinate

    return None
