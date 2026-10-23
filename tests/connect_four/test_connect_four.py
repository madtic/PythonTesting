import pytest

from testing_course.connect_four.connect_four_game import ConnectFourGame
from testing_course.connect_four.player import Player
from testing_course.connect_four.connect_four import InvalidMoveError

def test_board_size():
    game = ConnectFourGame(Player.RED)

    assert len(game.board) == 6

    for row in game.board:
        assert len(row) == 7

def test_empty_board():
    game = ConnectFourGame(Player.RED)

    for row in range(6):
        for col in range(7):
            assert game.get_player_at(row, col) == Player.NONE

def test_starting_player():
    game = ConnectFourGame(Player.RED)

    assert game.player_on_turn == Player.RED



def test_drop_piece():
    game = ConnectFourGame(Player.RED)

    game.drop(0)

    assert game.get_player_at(5, 0) == Player.RED

def test_stacking_pieces():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(0)

    assert game.get_player_at(5, 0) == Player.RED
    assert game.get_player_at(4, 0) == Player.YELLOW

def test_player_change():
    game = ConnectFourGame(Player.RED)

    assert game.player_on_turn == Player.RED

    game.drop(0)
    assert game.player_on_turn == Player.YELLOW

    game.drop(1)
    assert game.player_on_turn == Player.RED



def test_full_column():
    game = ConnectFourGame(Player.RED)

    for i in range(6):
        game.drop(0)

    current_player = game.player_on_turn

    with pytest.raises(InvalidMoveError):
        game.drop(0)

    assert game.player_on_turn == current_player

def test_invalid_column():
    game = ConnectFourGame(Player.RED)

    with pytest.raises(InvalidMoveError):
        game.drop(-4)

    with pytest.raises(InvalidMoveError):
        game.drop(9)



def test_reset_game():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(1)

    game.reset(Player.RED)

    for row in range(6):
        for col in range(7):
            assert game.get_player_at(row, col) == Player.NONE

def test_reset_player():
    game = ConnectFourGame(Player.RED)

    game.drop(0)

    game.reset(Player.YELLOW)

    assert game.player_on_turn == Player.YELLOW



def test_horizontal_win():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(0)
    game.drop(1)
    game.drop(1)
    game.drop(2)
    game.drop(2)
    game.drop(3)

    assert game.winner == Player.RED

def test_vertical_win():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)

    assert game.winner == Player.RED

def test_diagonal_win_right():
    game = ConnectFourGame(Player.RED)

    game.drop(0) #1
    game.drop(1)
    game.drop(1) #2
    game.drop(2)
    game.drop(4)
    game.drop(2)
    game.drop(2) #3
    game.drop(3)
    game.drop(4)
    game.drop(3)
    game.drop(5)
    game.drop(3)
    game.drop(3) #4

    assert game.winner == Player.RED

def test_diagonal_win_left():
    game = ConnectFourGame(Player.RED)

    game.drop(3) #1
    game.drop(2)
    game.drop(2) #2
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(1) #3
    game.drop(0)
    game.drop(0)
    game.drop(4)
    game.drop(0) #4

    assert game.winner == Player.RED

def test_no_winner():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(1)
    game.drop(2)
    game.drop(3)

    assert game.winner == Player.NONE


def test_game_not_over():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(1)

    assert game.is_game_over == False

def test_game_over_after_win():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(0)
    game.drop(1)
    game.drop(1)
    game.drop(2)
    game.drop(2)
    game.drop(3)

    assert game.is_game_over == True
    assert game.winner == Player.RED

def test_game_over_full_board():
    game = ConnectFourGame(Player.RED)

    pattern = [
        [1, 1, 2, 2, 1, 1, 2],
        [2, 2, 1, 1, 2, 2, 1],
        [1, 1, 2, 2, 1, 1, 2],
        [2, 2, 1, 1, 2, 2, 1],
        [1, 1, 2, 2, 1, 1, 2],
        [2, 2, 1, 1, 2, 2, 1]
    ]

    for row in range(6):
        for col in range(7):
            if pattern[row][col] == 1:
                game.board[row][col] = Player.RED
            else:
                game.board[row][col] = Player.YELLOW

    assert game.winner == Player.NONE
    assert game.is_game_over == True
    with pytest.raises(InvalidMoveError):
        game.drop(0)



def test_drop_after_game_over():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(0)
    game.drop(1)
    game.drop(1)
    game.drop(2)
    game.drop(2)
    game.drop(3)

    assert game.is_game_over == True

    with pytest.raises(InvalidMoveError):
        game.drop(4)



def test_yellow_win():
    game = ConnectFourGame(Player.YELLOW)

    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)

    assert game.winner == Player.YELLOW
    assert game.is_game_over == True



def test_reset_after_win():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(0)
    game.drop(1)
    game.drop(1)
    game.drop(2)
    game.drop(2)
    game.drop(3)

    assert game.is_game_over == True
    assert game.winner == Player.RED

    game.reset(Player.YELLOW)

    assert game.is_game_over == False
    assert game.winner == Player.NONE
    assert game.player_on_turn == Player.YELLOW

    game.drop(0)

    assert game.get_player_at(5, 0) == Player.YELLOW




def test_board_display():
    game = ConnectFourGame(Player.RED)

    game.drop(0)
    game.drop(1)

    rows = str(game).splitlines()

    assert len(rows) == 6
    assert rows[5] == "R Y _ _ _ _ _ "
    assert rows[0] == "_ _ _ _ _ _ _ "


def test_no_winner_empty_board():
    game = ConnectFourGame(Player.RED)

    assert game.winner == Player.NONE
    assert game.check_winner(Player.RED) == False
    assert game.check_winner(Player.NONE) == False
    assert game.check_winner(Player.YELLOW) == False


def test_player_after_invalid_move():
    game = ConnectFourGame(Player.RED)

    game.drop(0)

    assert game.player_on_turn == Player.YELLOW

    with pytest.raises(InvalidMoveError):
        game.drop(7)

    assert game.player_on_turn == Player.YELLOW
    assert game.get_player_at(5, 0) == Player.RED
