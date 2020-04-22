import random
from typing import Optional, Set

from board import Board, MOVES_BY_DIRECTION, MOVE_UP


def determine_move(board: Board) -> str:
    available_moves = board.available_moves()
    if len(available_moves) == 0:
        return MOVE_UP

    best_move = move_towards_largest_area(board, available_moves)
    return best_move


def move_towards_largest_area(board: Board, moves: Set[str]) -> str:
    sorted_directions = sorted([(move, board.area_value(move)) for move in moves], key=lambda x: x[1], reverse=True)
    return sorted_directions[0][0]


def random_move_without_collision(board: Board):
    # find coordinates I actually can move to
    return random.choice(list(board.available_moves()))


def move_from_direction(board: Board, direction: str) -> Optional[str]:
    moves = board.available_moves()
    moves_in_direction = MOVES_BY_DIRECTION[direction]
    good_moves = moves.intersection(moves_in_direction)
    if len(good_moves) > 0:
        return good_moves.pop()
    return None


def food_that_i_am_closest(board: Board) -> Optional[str]:
    sorted_food_coordinate_and_distance = sorted([
        (food_coord, board.my_head.distance(food_coord)) for food_coord in board.food_coordinates
    ], key=lambda e: e[1])

    for food_coordinate, distance in sorted_food_coordinate_and_distance:
        opponent_distances = [each.distance(food_coordinate) for each in board.opponent_heads]
        if all(each >= distance for each in opponent_distances):
            return move_from_direction(board, food_coordinate.direction_from(board.my_head))

    return None
