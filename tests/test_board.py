from board import Board, FOOD, EMPTY, SNAKE, DIRECTION_DOWN, DIRECTION_RIGHT, DIRECTION_UP, DIRECTION_LEFT, Coordinate, OTHER_SNAKE_HEAD, MY_HEAD
from tests.fixtures import MOVE_PAYLOAD


def test_init():
    height = 2
    width = 3
    board = Board.from_height_and_width(height=height, width=width)
    expected = {
        Coordinate(0, 0): '',
        Coordinate(0, 1): '',
        Coordinate(1, 0): '',
        Coordinate(1, 1): '',
        Coordinate(2, 0): '',
        Coordinate(2, 1): '',
    }
    assert expected == board.board


def test_update_board_with_food():
    board = Board.from_height_and_width(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["snakes"] = []
    board_data["board"]["food"] = [
        {
            "x": 2,
            "y": 1
        }
    ]
    board.update(board_data)
    assert board.board[Coordinate(0, 0)] == EMPTY
    assert board.board[Coordinate(0, 1)] == EMPTY
    assert board.board[Coordinate(0, 2)] == EMPTY
    assert board.board[Coordinate(1, 0)] == EMPTY
    assert board.board[Coordinate(1, 1)] == EMPTY
    assert board.board[Coordinate(1, 2)] == EMPTY
    assert board.board[Coordinate(2, 0)] == EMPTY
    assert board.board[Coordinate(2, 1)] == FOOD
    assert board.board[Coordinate(2, 2)] == EMPTY


def test_update_board_with_snakes():
    board = Board.from_height_and_width(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["food"] = []
    board_data["board"]["snakes"] = [
        {
            "id": "snake1",
            "body": [
                {
                    "x": 0,
                    "y": 0
                },
                {
                    "x": 1,
                    "y": 0
                },
            ]
        },
        {
            "id": "snake2",
            "body": [
                {
                    "x": 2,
                    "y": 2
                },
                {
                    "x": 2,
                    "y": 1
                },
            ]
        }
    ]

    board.update(board_data)

    assert board.board[Coordinate(0, 0)] == OTHER_SNAKE_HEAD
    assert board.board[Coordinate(0, 1)] == EMPTY
    assert board.board[Coordinate(0, 2)] == EMPTY
    assert board.board[Coordinate(1, 0)] == SNAKE
    assert board.board[Coordinate(1, 1)] == EMPTY
    assert board.board[Coordinate(1, 2)] == EMPTY
    assert board.board[Coordinate(2, 0)] == EMPTY
    assert board.board[Coordinate(2, 1)] == SNAKE
    assert board.board[Coordinate(2, 2)] == OTHER_SNAKE_HEAD


def test_moving_down():
    board = Board.from_height_and_width(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["snakes"] = []
    board_data["board"]["food"] = []
    board_data["you"] = {
        "body": [
                {
                    "x": 0,
                    "y": 1
                },
                {
                    "x": 0,
                    "y": 0
                },
            ]
    }
    board.update(board_data)
    assert board._my_direction == DIRECTION_DOWN
    assert board._my_head == Coordinate(0, 1)
    assert board._board[board._my_head] == MY_HEAD


def test_moving_right():
    board = Board.from_height_and_width(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["snakes"] = []
    board_data["board"]["food"] = []
    board_data["you"] = {
        "body": [
                {
                    "x": 1,
                    "y": 0
                },
                {
                    "x": 0,
                    "y": 0
                },
            ]
    }
    board.update(board_data)
    assert board._my_direction == DIRECTION_RIGHT
    assert board._my_head == Coordinate(1, 0)
    assert board._board[board._my_head] == MY_HEAD


def test_moving_up():
    board = Board.from_height_and_width(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["snakes"] = []
    board_data["board"]["food"] = []
    board_data["you"] = {
        "body": [
                {
                    "x": 0,
                    "y": 0
                },
                {
                    "x": 0,
                    "y": 1
                },
            ]
    }
    board.update(board_data)
    assert board._my_direction == DIRECTION_UP
    assert board._my_head == Coordinate(0, 0)
    assert board._board[board._my_head] == MY_HEAD


def test_moving_left():
    board = Board.from_height_and_width(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["snakes"] = []
    board_data["board"]["food"] = []
    board_data["you"] = {
        "body": [
                {
                    "x": 0,
                    "y": 0
                },
                {
                    "x": 1,
                    "y": 0
                },
            ]
    }
    board.update(board_data)
    assert board._my_direction == DIRECTION_LEFT
    assert board._my_head == Coordinate(0, 0)
    assert board._board[board._my_head] == MY_HEAD


def test_food_coordinates():
    board = Board.from_height_and_width(3, 3)
    board._board[Coordinate(0, 1)] = FOOD
    board._board[Coordinate(2, 2)] = FOOD
    board._board[Coordinate(1, 2)] = FOOD

    result = board.food_coordinates
    assert result == [
        Coordinate(0, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]


def test_opponent_heads():
    board = Board.from_height_and_width(3, 3)
    board._board[Coordinate(0, 1)] = OTHER_SNAKE_HEAD
    board._board[Coordinate(2, 2)] = OTHER_SNAKE_HEAD
    board._board[Coordinate(1, 2)] = OTHER_SNAKE_HEAD

    result = board.opponent_heads
    assert result == [
        Coordinate(0, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
