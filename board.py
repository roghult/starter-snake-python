EMPTY = ''
SNAKE = 'S'
FOOD = 'F'
UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


class Board:

    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._board = {(x, y): EMPTY for x in range(width) for y in range(height)}
        self._my_head = None
        self._my_direction = None

    @property
    def board(self):
        return self._board

    def update(self, board_data):
        self._update_food(board_data)
        self._update_snakes(board_data)
        self._update_my_snake(board_data)

    def _update_food(self, board_data):
        food_coordinates = board_data["board"]["food"]
        for coordinates in food_coordinates:
            coordinate = (coordinates["x"], coordinates["y"])
            self._board[coordinate] = FOOD

    def _update_snakes(self, board_data):
        snake_data = board_data["board"]["snakes"]
        l = [data["body"] for data in snake_data]
        snake_coordinates = [item for sublist in l for item in sublist]
        for coordinates in snake_coordinates:
            coordinate = (coordinates["x"], coordinates["y"])
            self._board[coordinate] = SNAKE

    def _update_my_snake(self, board_data):
        my_snake = board_data["you"]["body"]
        if len(my_snake) == 1:
            self._my_direction = None
        else:
            head, body = my_snake[:2]
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
