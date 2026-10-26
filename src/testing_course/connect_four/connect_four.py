from typing import Protocol

from testing_course.connect_four.player import Player

#############################
# Is the Interface for the Connect Four Game. It defines the methods and properties that any implementation of
# the game should have. The ConnectFourGame class is an example of a concrete implementation of this interface.
################################


class InvalidMoveError(Exception):
    """Raised when a disc cannot be dropped (full column or finished game)."""


class ConnectFour(Protocol):
    def get_player_at(self, row: int, col: int) -> Player: ...

    @property
    def player_on_turn(self) -> Player: ...

    @property
    def is_game_over(self) -> bool: ...

    @property
    def is_tie(self) -> bool: ...

    @property
    def winner(self) -> Player: ...

    def reset(self, player_on_turn: Player) -> None: ...

    def drop(self, col: int) -> None: ...
