from board import Board, FOOD, EMPTY, SNAKE, DOWN, RIGHT, UP, LEFT, Coordinate, HEAD
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

    assert board.board[Coordinate(0, 0)] == HEAD
    assert board.board[Coordinate(0, 1)] == EMPTY
    assert board.board[Coordinate(0, 2)] == EMPTY
    assert board.board[Coordinate(1, 0)] == SNAKE
    assert board.board[Coordinate(1, 1)] == EMPTY
    assert board.board[Coordinate(1, 2)] == EMPTY
    assert board.board[Coordinate(2, 0)] == EMPTY
    assert board.board[Coordinate(2, 1)] == SNAKE
    assert board.board[Coordinate(2, 2)] == HEAD


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
    assert board._my_direction == DOWN


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
    assert board._my_direction == RIGHT


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
    assert board._my_direction == UP


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
    assert board._my_direction == LEFT
