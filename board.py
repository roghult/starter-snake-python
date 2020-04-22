from typing import Dict, List, Optional, Set

EMPTY = ''
SNAKE = 'S'
MY_HEAD = 'MH'
OTHER_SNAKE_HEAD = 'H'
FOOD = 'F'
DIRECTION_UP = 'U'
DIRECTION_DOWN = 'D'
DIRECTION_LEFT = 'L'
DIRECTION_RIGHT = 'R'
DIRECTION_UP_RIGHT = 'UR'
DIRECTION_DOWN_RIGHT = 'DR'
DIRECTION_DOWN_LEFT = 'DL'
DIRECTION_UP_LEFT = 'UL'
MOVABLE_DIRECTIONS = [DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT]

MOVE_UP = "up"
MOVE_DOWN = "down"
MOVE_LEFT = "left"
MOVE_RIGHT = "right"
ALL_MOVES = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]

MOVES_BY_DIRECTION = {
    DIRECTION_UP: {MOVE_UP},
    DIRECTION_DOWN: {MOVE_DOWN},
    DIRECTION_RIGHT: {MOVE_RIGHT},
    DIRECTION_LEFT: {MOVE_LEFT},
    DIRECTION_UP_RIGHT: {MOVE_UP, MOVE_RIGHT},
    DIRECTION_DOWN_RIGHT: {MOVE_DOWN, MOVE_RIGHT},
    DIRECTION_DOWN_LEFT: {MOVE_DOWN, MOVE_LEFT},
    DIRECTION_UP_LEFT: {MOVE_UP, MOVE_LEFT},
}


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

    def move(self, move: str) -> "Coordinate":
        x = self.x
        y = self.y
        if move == MOVE_UP:
            y -= 1
        elif move == MOVE_DOWN:
            y += 1
        elif move == MOVE_LEFT:
            x -= 1
        elif move == MOVE_RIGHT:
            x += 1
        return Coordinate(x, y)

    def distance(self, coordinate: 'Coordinate') -> int:
        return abs(self._x - coordinate._x) + abs(self._y - coordinate._y)

    def direction_from(self, coordinate: 'Coordinate') -> str:
        x_diff = self.x - coordinate.x
        y_diff = self.y - coordinate.y
        if x_diff > 0 > y_diff:
            return DIRECTION_UP_RIGHT
        elif x_diff > 0 and y_diff > 0:
            return DIRECTION_DOWN_RIGHT
        elif x_diff < 0 < y_diff:
            return DIRECTION_DOWN_LEFT
        elif x_diff < 0 and y_diff < 0:
            return DIRECTION_UP_LEFT
        elif x_diff < 0:
            return DIRECTION_LEFT
        elif x_diff > 0:
            return DIRECTION_RIGHT
        elif y_diff > 0:
            return DIRECTION_DOWN
        elif y_diff < 0:
            return DIRECTION_UP
        else:
            return None

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
        self._my_head: Optional[Coordinate] = None
        self._my_direction = None

    @classmethod
    def from_height_and_width(cls, height: int, width: int):
        starting_board = {Coordinate(x, y): EMPTY for x in range(width) for y in range(height)}
        return cls(starting_board)

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

    def area_value(self, move: str) -> int:
        """
        Calculates the value for the are available in the given direction
        from the head. The value is the sum of all values for nodes that can
        be visited. A node value is calculated as follows:
        0p: there are no exits from the node
        1p: there is one exit from the node
        2p: there is more than one exit from the node
        +0.5p: if the node contains FOOD
        """
        value = 0
        start = self.my_head.move(move)
        queue = [start]
        visited = set()
        while queue:
            coordinate = queue.pop(0)
            visited.add(coordinate)
            moves = self.available_moves(coordinate)
            if self._board[coordinate] == FOOD:
                value += 0.5
            if len(moves) == 2:
                value += 1
            if len(moves) > 2:
                value += 2
            move_coordinates = [coordinate.move(move) for move in moves]
            move_coordinates = [each for each in move_coordinates if each not in visited and each not in queue]
            queue.extend(move_coordinates)
        return value

    def available_moves(self, origin=None) -> Set[str]:
        return {move for move in ALL_MOVES if self.can_move(move, origin)}

    def can_move(self, move: str, origin=None) -> bool:
        if origin is None:
            origin = self._my_head
        coordinate = origin.move(move)
        in_direction = self._board.get(coordinate)
        return in_direction in [FOOD, EMPTY]

    def update(self, board_data):
        self._clean_board()
        self._update_food(board_data)
        self._update_snakes(board_data)
        self._update_my_snake(board_data)

    def _clean_board(self):
        for key in self._board.keys():
            self._board[key] = EMPTY

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
            head_coordinate = Coordinate(head['x'], head['y'])
            body_coordinate = Coordinate(body['x'], body['y'])
            self._my_direction = head_coordinate.direction_from(body_coordinate)
