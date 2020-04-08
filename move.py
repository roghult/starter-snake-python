import random
from typing import Optional, Set

from board import Board, ALL_MOVES, MOVES_BY_DIRECTION


def determine_move(board: Board) -> str:
    closest_food_coordinate = food_that_i_am_closest(board)
    if closest_food_coordinate is None:
        move_in_direction = random_move_without_collision(board)
    else:
        move_in_direction = closest_food_coordinate
    return move_in_direction


def available_moves(board: Board) -> Set[str]:
    return {move for move in ALL_MOVES if board.can_move(move)}


def random_move_without_collision(board: Board):
    # find coordinates I actually can move to
    return random.choice(list(available_moves(board)))


def move_from_direction(board: Board, direction: str) -> Optional[str]:
    moves = available_moves(board)
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
