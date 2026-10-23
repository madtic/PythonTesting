from testing_course.connect_four.player import Player
from testing_course.connect_four.connect_four import InvalidMoveError


class ConnectFourGame:
    def __init__(self, player_on_turn: Player) -> None:
        self.board = []

        for row in range(6):
            self.board.append([Player.NONE] * 7)

        self._player_on_turn = player_on_turn

    def get_player_at(self, row: int, col: int) -> Player:
        return self.board[row][col]

    @property
    def player_on_turn(self) -> Player:
        return self._player_on_turn

    @property
    def is_game_over(self) -> bool:
        if self.winner != Player.NONE:
            return True

        for col in range(7):
            if self.board[0][col] == Player.NONE:
                return False

        return True

    @property
    def winner(self) -> Player:
        if self.check_winner(Player.RED):
            return Player.RED
        
        elif self.check_winner(Player.YELLOW):
            return Player.YELLOW
        
        else:
            return Player.NONE
        

    def reset(self, player_on_turn: Player) -> None:
        self.board = []

        for row in range(6):
            self.board.append([Player.NONE] * 7)

        self._player_on_turn = player_on_turn

    def drop(self, col: int) -> None:
        if self.is_game_over:
            raise InvalidMoveError("Game is already over")

        if col < 0 or col > 6:
            raise InvalidMoveError("Invalid column")

        for row in range(5, -1, -1):
            if self.board[row][col] == Player.NONE:
                self.board[row][col] = self._player_on_turn

                if self._player_on_turn == Player.RED:
                    self._player_on_turn = Player.YELLOW
                
                else:
                    self._player_on_turn = Player.RED
            
                return

        raise InvalidMoveError("Column is full")

    def check_winner(self, player: Player) -> bool:
        if player == Player.NONE:
            return False

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for row in range(6):
            for col in range(7):
                if self.board[row][col] != player:
                    continue

                for dr, dc in directions:
                    count = 0

                    for i in range(4):
                        r = row + dr * i
                        c = col + dc * i

                        if 0 <= r < 6 and 0 <= c < 7:
                            if self.board[r][c] == player:
                                count += 1

                    if count == 4:
                        return True

        return False

    
    def __str__(self) -> str:
        text = ""

        for row in self.board:
            for cell in row:
                if cell == Player.RED:
                    text += "R "
                elif cell == Player.YELLOW:
                    text += "Y "
                else:
                    text += "_ "

            text += "\n"

        return text

                         