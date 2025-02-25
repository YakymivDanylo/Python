emptyField = "X"
chessBoard = [[emptyField] * 8 for i in range(8)]

blackQueen = "♛"
blackRook = "♜"
whiteKnight = "♘"

blackQueenMove = "Q"
blackRookMove = "R"
whiteKnightMove = "K"


def printBoard():
    for i in range(8):
        for j in range(8):
            print(f"{chessBoard[i][j]}\t\t", end="")
        print()
        print()


def putQueen(x, y):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    if chessBoard[x][y] == emptyField:
        chessBoard[x][y] = blackQueen
    elif chessBoard[x][y] in (blackRookMove, whiteKnightMove):
        chessBoard[x][y] += blackQueen

    for dx, dy in moves:
        new_x, new_y = x, y

        while 0 <= new_x + dx < 8 and 0 <= new_y + dy < 8:
            new_x += dx
            new_y += dy

            if chessBoard[new_x][new_y] == emptyField:
                chessBoard[new_x][new_y] = blackQueenMove
            else:
                chessBoard[new_x][new_y] += blackQueenMove


def putRook(x, y):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if chessBoard[x][y] == emptyField:
        chessBoard[x][y] = blackRook
    elif chessBoard[x][y] in (blackQueenMove, whiteKnightMove):
        chessBoard[x][y] += blackRook

    for dx, dy in moves:
        new_x, new_y = x, y

        while 0 <= new_x + dx < 8 and 0 <= new_y + dy < 8:
            new_x += dx
            new_y += dy

            if chessBoard[new_x][new_y] == emptyField:
                chessBoard[new_x][new_y] = blackRookMove
            else:
                chessBoard[new_x][new_y] += blackRookMove


def putKnight(x, y):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    if chessBoard[x][y] == emptyField:
        chessBoard[x][y] = whiteKnight
    elif chessBoard[x][y] in (blackQueenMove, blackRookMove):
        chessBoard[x][y] += whiteKnight

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < 8 and 0 <= new_y < 8:
            if chessBoard[new_x][new_y] == emptyField:
                chessBoard[new_x][new_y] = whiteKnightMove
            else:
                chessBoard[new_x][new_y] += whiteKnightMove


def moveForBlackQueen():
    combination_moves = []
    hit_combinations = []
    for x in range(8):
        for y in range(8):
            if blackQueenMove in chessBoard[x][y] and blackRook not in chessBoard[x][y] and whiteKnight not in \
                    chessBoard[x][y]:
                combination_moves.append((x, y))
            elif whiteKnight in chessBoard[x][y] and blackQueenMove in chessBoard[x][y]:
                hit_combinations.append((x, y))

    print("Black Queen can move to: ")
    for i, j in combination_moves:
        print(f"({j + 1}, {8 - i})", end=" ")  # Зміна формату координат
    print()

    print("Black Queen can hit: ")
    for i, j in hit_combinations:
        print(f"({j + 1}, {8 - i})", end="")


def moveForBlackRook():
    combination_moves = []
    hit_combinations = []

    for x in range(8):
        for y in range(8):
            if blackRookMove in chessBoard[x][y] and whiteKnight not in chessBoard[x][y] and blackQueen not in \
                    chessBoard[x][y]:
                combination_moves.append((x, y))
            elif whiteKnight in chessBoard[x][y]:
                hit_combinations.append((x, y))

    print("Black Rook can move to: ")
    for i, j in combination_moves:
        print(f"({j + 1}, {8 - i})", end=" ")
    print()

    print("Black Rook can hit: ")
    for i, j in hit_combinations:
        print(f"({j + 1}, {8 - i})", end="")
    print()


def moveForWhiteKnight():
    combination_moves = []
    hit_combinations = []

    for x in range(8):
        for y in range(8):
            if whiteKnightMove in chessBoard[x][y] and blackRook not in chessBoard[x][y] and blackQueen not in \
                    chessBoard[x][y]:
                combination_moves.append((x, y))
            elif (blackRook in chessBoard[x][y] and whiteKnightMove in chessBoard[x][y]) or (
                    blackQueen in chessBoard[x][y] and whiteKnightMove in chessBoard[x][y]):
                hit_combinations.append((x, y))

    print(f"White Knight can move to: ")
    for i, j in combination_moves:
        print(f"({j + 1}, {8 - i})", end=" ")
    print()

    print("White Knight can hit: ")
    for i, j in hit_combinations:
        print(f"({j + 1}, {8 - i})", end="")
    print()


def game():
    print("Welcome\n Before starting the game you have to point the coordinates of each figure\n")
    print("Enter the horizontal coordinates of Black Queen: ")
    queen_x = int(input())
    print("Enter the vertical coordinates of Black Queen: ")
    queen_y = int(input())
    putQueen(8 - queen_y, queen_x - 1)  # Зміна порядку координат
    printBoard()

    while True:
        print("Enter the horizontal coordinates of Black Rook: ")
        rook_x = int(input())
        print("Enter the vertical coordinates of Black Rook: ")
        rook_y = int(input())
        if chessBoard[8 - rook_y][rook_x - 1] != blackQueen:
            putRook(8 - rook_y, rook_x - 1)  # Зміна порядку координат
            printBoard()
            break
        else:
            print("Enter again")

    while True:
        print("Enter the horizontal coordinates of White Knight: ")
        knight_x = int(input())
        print("Enter the vertical coordinates of White Knight: ")
        knight_y = int(input())
        if (chessBoard[8 - knight_y][knight_x - 1] != blackQueen and chessBoard[8 - knight_y][
            knight_x - 1] != blackRook):
            putKnight(8 - knight_y, knight_x - 1)  # Зміна порядку координат
            printBoard()
            break
        else:
            print("Enter again")

    while True:
        print("Choose the figure to possible actions")
        print("Q - Queen")
        print("R - Rook")
        print("K - Knight")
        choose = input()
        if choose.upper() == "Q":
            moveForBlackQueen()
            break
        elif choose.upper() == "R":
            moveForBlackRook()
            break
        elif choose.upper() == "K":
            moveForWhiteKnight()
            break
        else:
            print("Enter again")


if __name__ == "__main__":
    game()
