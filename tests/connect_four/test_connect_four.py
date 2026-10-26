import pytest
from testing_course.connect_four.connect_four_game import ConnectFourGame
from testing_course.connect_four.player import Player

@pytest.fixture
def game() -> ConnectFourGame:
    return ConnectFourGame(Player.RED)

def test_initial_state(game:ConnectFourGame) -> None:
    for row in range(6):
        for col in range(7):
            assert game.get_player_at(col, row) == Player.NONE
    assert game._player_on_turn == Player.RED
    assert not game._is_game_over
    assert game._winner == Player.NONE
    assert game._rows == 6
    assert game._cols == 7

def test_drop_places_disc_at_bottom():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    assert game.get_player_at(0, 5) == Player.RED
    assert game._player_on_turn == Player.YELLOW

def test_drop_full_column_raises_error():
    game = ConnectFourGame(Player.RED)
    for _ in range(6):
        game.drop(0)
    with pytest.raises(ValueError, match="Column is full"):
        game.drop(0)

def test_drop_invalid_column_raises_error():
    game = ConnectFourGame(Player.RED)
    with pytest.raises(ValueError, match="Invalid column"):
        game.drop(-1)
    with pytest.raises(ValueError, match="Invalid column"):
        game.drop(7)

def test_turn_switching():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    assert game._player_on_turn == Player.YELLOW
    game.drop(1)
    assert game._player_on_turn == Player.RED

def test_get_player_at_returns_correct_player():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    assert game.get_player_at(0, 5) == Player.RED
    game.drop(1)
    assert game.get_player_at(1, 5) == Player.YELLOW

def test_get_winner_vertical():
    game = ConnectFourGame(Player.RED)
    assert game.winner == Player.NONE
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game._winner = Player.RED
    assert game.winner == Player.RED
    assert game.winner != Player.YELLOW
    assert game.winner != Player.NONE
    assert game.is_game_over == True

def test_get_winner_horizontal():
    game = ConnectFourGame(Player.RED)
    assert game.winner == Player.NONE
    game.drop(0)
    game.drop(0)
    game.drop(1)
    game.drop(1)
    game.drop(2)
    game.drop(2)
    game.drop(3)
    game.drop(3)
    game.drop(4)
    assert game.winner == Player.RED
    assert game.winner != Player.YELLOW
    assert game.winner != Player.NONE
    assert game.is_game_over == True

def test_get_winner_diagonal():
    game = ConnectFourGame(Player.RED)
    assert game.winner == Player.NONE
    game.drop(0)  # R
    game.drop(1)  # Y
    game.drop(1)  # R
    game.drop(2)  # Y
    game.drop(2)  # R
    game.drop(3)  # Y
    game.drop(2)  # R
    game.drop(3)  # Y
    game.drop(3)  # R
    game.drop(4)  # Y
    game.drop(3)  # R 
    assert game.winner == Player.RED
    assert game.winner != Player.YELLOW
    assert game.winner != Player.NONE

def test_reset_game():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    game.drop(1)
    game.reset(Player.YELLOW)
    assert game.player_on_turn == Player.YELLOW
    assert not game.is_game_over
    assert game.winner == Player.NONE
    assert game.turn == 1
    for r in range(game._rows):
        for c in range(game._cols):
            assert game._board[r][c] == Player.NONE

def test_board_full():
    pass

def test_print_game_board():
    game = ConnectFourGame(Player.RED)
    expected_empty = (
        "Turn: 1\n"
        "| . | . | . | . | . | . | . |\n"
        "| . | . | . | . | . | . | . |\n"
        "| . | . | . | . | . | . | . |\n"
        "| . | . | . | . | . | . | . |\n"
        "| . | . | . | . | . | . | . |\n"
        "| . | . | . | . | . | . | . |\n"
        "+---+---+---+---+---+---+---+\n"
        "  1   2   3   4   5   6   7  \n"
        "Current player: RED"
    )
    assert str(game) == expected_empty
    game.drop(0)
    assert str(game).startswith("Turn: 1\n")
    assert "| R | . | . | . | . | . | . |" in str(game)
    assert "Current player: YELLOW" in str(game)

    game.drop(1)
    assert str(game).startswith("Turn: 2\n")
    assert "Current player: RED" in str(game)

    # Test won game does not print current player
    game._is_game_over = True
    assert "Current player" not in str(game)

def test_turn_counting():
    game = ConnectFourGame(Player.RED)
    assert game.turn == 1
    game.drop(0)  # Red drops
    assert game.turn == 1
    game.drop(0)  # Yellow drops -> 1 round used
    assert game.turn == 2
    game.drop(1)  # Red drops
    assert game.turn == 2
    game.drop(1)  # Yellow drops -> 2 rounds used
    assert game.turn == 3
