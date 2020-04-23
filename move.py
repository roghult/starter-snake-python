import random
from typing import Optional, Set, List, Tuple

from board import Board, MOVES_BY_DIRECTION, MOVE_UP


def determine_move(board: Board) -> str:
    available_moves = board.available_moves()
    if len(available_moves) == 0:
        return MOVE_UP

    sorted_moves = moves_sorted_by_area_rank(board, available_moves)
    available_moves = filter_out_bad_moves(board, sorted_moves)

    closest_food_coordinate = food_that_i_am_closest(board, available_moves)
    if closest_food_coordinate is None:
        move_in_direction = random_move_without_collision(board, available_moves)
    else:
        move_in_direction = closest_food_coordinate
    return move_in_direction


def filter_out_bad_moves(board: Board, sorted_moves: List[Tuple[str, int]]) -> Set[str]:
    return {each[0] for each in sorted_moves if each[1] > board.my_length}


def moves_sorted_by_area_rank(board: Board, moves: Set[str]) -> List[Tuple[str, int]]:
    sorted_moves = sorted([(move, board.area_rank(move)) for move in moves], key=lambda x: x[1], reverse=True)
    return sorted_moves


def random_move_without_collision(board: Board, available_moves: Set[str]):
    # find coordinates I actually can move to
    if len(available_moves) == 0:
        available_moves = board.available_moves()
    return random.choice(list(available_moves))


def move_from_direction(direction: str, available_moves: Set[str]) -> Optional[str]:
    moves_in_direction = MOVES_BY_DIRECTION[direction]
    good_moves = available_moves.intersection(moves_in_direction)
    if len(good_moves) > 0:
        return good_moves.pop()
    return None


def food_that_i_am_closest(board: Board, available_moves: Set[str]) -> Optional[str]:
    sorted_food_coordinate_and_distance = sorted([
        (food_coord, board.my_head.distance(food_coord)) for food_coord in board.food_coordinates
    ], key=lambda e: e[1])

    for food_coordinate, distance in sorted_food_coordinate_and_distance:
        opponent_distances = [each.distance(food_coordinate) for each in board.opponent_heads]
        if all(each >= distance for each in opponent_distances):
            return move_from_direction(food_coordinate.direction_from(board.my_head), available_moves)

    return None
