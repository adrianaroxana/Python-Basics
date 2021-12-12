def print_board(board):
    rows = len(board)
    cols = len(board[0])
    last_col = cols + 5
    for row in range(rows):
        for col in range(cols + 6):
            if col % 2 == 0:
                practical_column = int(col / 2)
                if col != last_col:
                    print(board[row][practical_column], end="")
                else:
                    print(board[row][practical_column])
            else:
                print("|", end="")


def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == " ":
            row[column] = piece
            return True
    return False


def winner(board, piece):
    rows = len(board)
    cols = len(board[0])
    # Check horizontal locations for win
    for col in range(cols - 3):
        for row in range(rows):
            if (
                board[row][col] == piece
                and board[row][col + 1] == piece
                and board[row][col + 2] == piece
                and board[row][col + 3] == piece
            ):
                return True

    # Check vertical locations for win
    for col in range(cols):
        for row in range(rows - 3):
            if (
                board[row][col] == piece
                and board[row + 1][col] == piece
                and board[row + 2][col] == piece
                and board[row + 3][col] == piece
            ):
                return True

    # Check positively sloped diaganols
    for col in range(cols - 3):
        for row in range(rows - 3):
            if (
                board[row][col] == piece
                and board[row + 1][col + 1] == piece
                and board[row + 2][col + 2] == piece
                and board[row + 3][col + 3] == piece
            ):
                return True

    # Check negatively sloped diaganols
    for col in range(cols - 3):
        for row in range(3, rows):
            if (
                board[row][col] == piece
                and board[row - 1][col + 1] == piece
                and board[row - 2][col + 2] == piece
                and board[row - 3][col + 3] == piece
            ):
                return True


def main():
    play_board = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]

    print_board(play_board)
    player = 1
    piece = "X"
    while not winner(play_board, piece):
        if player == 1:
            print("It's player's " + str(player) + " turn.")
            move = int(input("Please choose a column: "))
            drop_piece(play_board, move - 1, piece)
            if winner(play_board, piece):
                print("The winner is player: ", player)
                break
            piece = "O"
            player = 2
        else:
            print("It's player's " + str(player) + " turn.")
            move = int(input("Please choose a column: "))
            drop_piece(play_board, move - 1, piece)
            if winner(play_board, piece):
                print("The winner is player: ", player)
                break
            piece = "X"
            player = 1
        print_board(play_board)
    print_board(play_board)


if __name__ == "__main__":
    main()
