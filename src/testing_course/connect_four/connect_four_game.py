from testing_course.connect_four.player import Player


class ConnectFourGame:
    def __init__(self, player_on_turn: Player) -> None:
        self._player_on_turn = player_on_turn
        self._is_game_over = False
        self._winner = Player.NONE
        self._rows = 6
        self._cols = 7
        self._drops = 0
        # Initialize an empty 6x7 board
        self._board = [
            [Player.NONE for _ in range(self._cols)] for _ in range(self._rows)
        ]

    def get_player_at(self, row: int, col: int) -> Player:
        return self._board[row][col]

    @property
    def turn(self) -> int:
        return (self._drops // 2) + 1

    @property
    def round(self) -> int:
        return self.turn

    def __str__(self) -> str:
        symbol_map = {
            Player.NONE: ".",
            Player.RED: "R",
            Player.YELLOW: "Y",
        }
        lines = [f"Turn: {self.turn}"]
        for row in self._board:
            lines.append("| " + " | ".join(symbol_map[cell] for cell in row) + " |")
        lines.append("+---" * self._cols + "+")
        lines.append("  " + "   ".join(str(i + 1) for i in range(self._cols)) + "  ")
        if not self.is_game_over:
            lines.append(f"Current player: {self._player_on_turn.name}")
        return "\n".join(lines)

    def print_board(self) -> None:
        print(self)

    @property
    def player_on_turn(self) -> Player:
        return self._player_on_turn

    @property
    def is_game_over(self) -> bool:
        if self._is_game_over:
            return True

        for player in (Player.RED, Player.YELLOW):
            # Horizontal
            for row in range(self._rows):
                for col in range(self._cols - 3):
                    if (
                        self._board[row][col] == player
                        and self._board[row][col + 1] == player
                        and self._board[row][col + 2] == player
                        and self._board[row][col + 3] == player
                    ):
                        self._winner = player
                        self._is_game_over = True
                        return True

            # Vertikal
            for row in range(self._rows - 3):
                for col in range(self._cols):
                    if (
                        self._board[row][col] == player
                        and self._board[row + 1][col] == player
                        and self._board[row + 2][col] == player
                        and self._board[row + 3][col] == player
                    ):
                        self._winner = player
                        self._is_game_over = True
                        return True

            # Diagonal links-oben nach rechts-unten (\)
            for row in range(self._rows - 3):
                for col in range(self._cols - 3):
                    if (
                        self._board[row][col] == player
                        and self._board[row + 1][col + 1] == player
                        and self._board[row + 2][col + 2] == player
                        and self._board[row + 3][col + 3] == player
                    ):
                        self._winner = player
                        self._is_game_over = True
                        return True

            # Diagonal links-unten nach rechts-oben (/)
            for row in range(3, self._rows):
                for col in range(self._cols - 3):
                    if (
                        self._board[row][col] == player
                        and self._board[row - 1][col + 1] == player
                        and self._board[row - 2][col + 2] == player
                        and self._board[row - 3][col + 3] == player
                    ):
                        self._winner = player
                        self._is_game_over = True
                        return True

        # Unentschieden (Spielfeld komplett voll)
        is_full = all(
            self._board[r][c] != Player.NONE
            for r in range(self._rows)
            for c in range(self._cols)
        )
        if is_full:
            self._winner = Player.NONE
            self._is_game_over = True
            return True

        return False

    @property
    def winner(self) -> Player:
        if self._winner == Player.NONE:
            _ = self.is_game_over
        return self._winner

    @property
    def is_tie(self) -> bool:
        return self.is_game_over and self.winner == Player.NONE

    def reset(self, player_on_turn: Player) -> None:
        self._player_on_turn = player_on_turn
        self._is_game_over = False
        self._winner = Player.NONE
        self._drops = 0
        self._board = [
            [Player.NONE for _ in range(self._cols)] for _ in range(self._rows)
        ]

    def drop(self, col: int) -> None:
        # Check if the column is valid
        if col < 0 or col >= self._cols:
            raise ValueError("Invalid column")

        # Find the lowest empty row in the specified column
        for row in reversed(range(self._rows)):
            if self._board[row][col] == Player.NONE:
                self._board[row][col] = self._player_on_turn
                self._drops += 1
                # Switch turns
                self._player_on_turn = (
                    Player.YELLOW if self._player_on_turn == Player.RED else Player.RED
                )
                return

        # If the column is full, raise an error
        raise ValueError("Column is full")
