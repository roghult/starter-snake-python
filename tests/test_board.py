from board import Board, FOOD, EMPTY, SNAKE, DOWN, RIGHT, UP, LEFT
from tests.fixtures import MOVE_PAYLOAD


def test_init():
    height = 2
    width = 3
    board = Board(height=height, width=width)
    expected = {
        (0, 0): '',
        (0, 1): '',
        (1, 0): '',
        (1, 1): '',
        (2, 0): '',
        (2, 1): '',
    }
    assert expected == board.board


def test_update_board_with_food():
    board = Board(height=3, width=3)
    board_data = MOVE_PAYLOAD
    board_data["board"]["snakes"] = []
    board_data["board"]["food"] = [
        {
            "x": 2,
            "y": 1
        }
    ]
    board.update(board_data)
    assert board.board[(0, 0)] == EMPTY
    assert board.board[(0, 1)] == EMPTY
    assert board.board[(0, 2)] == EMPTY
    assert board.board[(1, 0)] == EMPTY
    assert board.board[(1, 1)] == EMPTY
    assert board.board[(1, 2)] == EMPTY
    assert board.board[(2, 0)] == EMPTY
    assert board.board[(2, 1)] == FOOD
    assert board.board[(2, 2)] == EMPTY


def test_update_board_with_snakes():
    board = Board(height=3, width=3)
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

    assert board.board[(0, 0)] == SNAKE
    assert board.board[(0, 1)] == EMPTY
    assert board.board[(0, 2)] == EMPTY
    assert board.board[(1, 0)] == SNAKE
    assert board.board[(1, 1)] == EMPTY
    assert board.board[(1, 2)] == EMPTY
    assert board.board[(2, 0)] == EMPTY
    assert board.board[(2, 1)] == SNAKE
    assert board.board[(2, 2)] == SNAKE


def test_moving_down():
    board = Board(height=3, width=3)
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
    board = Board(height=3, width=3)
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
    board = Board(height=3, width=3)
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
    board = Board(height=3, width=3)
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
