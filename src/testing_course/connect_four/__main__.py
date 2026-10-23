from testing_course.connect_four.connect_four import ConnectFour
from testing_course.connect_four.connect_four_game import ConnectFourGame
from testing_course.connect_four.player import Player
from testing_course.connect_four.connect_four import InvalidMoveError

HELP = """
Available commands:
-------------------
1 .. 7 --> drop disc in column
r      --> restart game
q      --> quit game
h      --> show help"""


def main() -> None:
    game: ConnectFour = ConnectFourGame(Player.RED)
    print(game)

    while not game.is_game_over:
        try:
            command = input("command [1 .. 7, (r)estart, (q)uit, (h)elp] > ")
        except EOFError:
            return

        match command:
            case "1" | "2" | "3" | "4" | "5" | "6" | "7":
                try:
                    game.drop(int(command) - 1)
                except InvalidMoveError as e:
                    print(f"Error: {e}")
            case "r":
                game.reset(Player.RED)
            case "q":
                print("Ok, bye.")
                return
            case "h":
                print(HELP)
            case _:
                print("Unknown command")
        print(game)

    if game.winner == Player.NONE:
        print("GAME OVER - Draw!")
    else:
        print(f"GAME OVER - Winner: {game.winner.name}")


if __name__ == "__main__":
    main()
