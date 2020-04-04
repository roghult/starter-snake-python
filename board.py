from typing import Dict, List

EMPTY = ''
SNAKE = 'S'
MY_HEAD = 'MH'
OTHER_SNAKE_HEAD = 'H'
FOOD = 'F'
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


class Coordinate:
    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def distance(self, coordinate: 'Coordinate') -> int:
        return abs(self._x - coordinate._x) + abs(self._y - coordinate._y)

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other: 'Coordinate'):
        return (self._x, self._y) == (other._x, other._y)

    def __str__(self):
        return "({}, {})".format(self._x, self._y)

    def __repr__(self):
        return self.__str__()


class Board:

    def __init__(self, starting_board: Dict[Coordinate, str]):
        self._board = starting_board
        self._my_head = None
        self._my_direction = None

    @property
    def my_head(self) -> Coordinate:
        return self._my_head

    @property
    def board(self):
        return self._board

    @property
    def food_coordinates(self) -> List[Coordinate]:
        return [key for (key, value) in self._board.items() if value == FOOD]

    @property
    def opponent_heads(self) -> List[Coordinate]:
        return [key for (key, value) in self._board.items() if value == OTHER_SNAKE_HEAD]

    @classmethod
    def from_height_and_width(cls, height: int, width: int):
        starting_board = {Coordinate(x, y): EMPTY for x in range(width) for y in range(height)}
        return cls(starting_board)

    def update(self, board_data):
        self._update_food(board_data)
        self._update_snakes(board_data)
        self._update_my_snake(board_data)

    def _update_food(self, board_data):
        food_coordinates = board_data["board"]["food"]
        for coordinates in food_coordinates:
            coordinate = Coordinate(coordinates["x"], coordinates["y"])
            self._board[coordinate] = FOOD

    def _update_snakes(self, board_data):
        snake_data = board_data["board"]["snakes"]
        snakes_coordinates = [data["body"] for data in snake_data]
        for snake_coordinates in snakes_coordinates:
            head_coordinate = snake_coordinates[0]
            self._board[Coordinate(head_coordinate["x"], head_coordinate["y"])] = OTHER_SNAKE_HEAD
            for body_coordinate in snake_coordinates[1:]:
                self._board[Coordinate(body_coordinate["x"], body_coordinate["y"])] = SNAKE

    def _update_my_snake(self, board_data):
        my_snake_coordinates = board_data["you"]["body"]
        my_head_coordinates = my_snake_coordinates[0]
        self._my_head = Coordinate(my_head_coordinates["x"], my_head_coordinates["y"])
        self._board[self._my_head] = MY_HEAD
        if len(my_snake_coordinates) == 1:
            self._my_direction = None
        else:
            head, body = my_snake_coordinates[:2]
            self._my_direction = self._direction(head, body)

    def _direction(self, head, body):
        x_diff = head['x'] - body['x']
        y_diff = head['y'] - body['y']
        if x_diff < 0:
            return LEFT
        elif x_diff > 0:
            return RIGHT
        elif y_diff > 0:
            return DOWN
        elif y_diff < 0:
            return UP
        else:
            return SNAKE
