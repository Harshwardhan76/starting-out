

def display_board(board):
    try:
        print(f"\n {board[0]} | {board[1]} | {board[2]} ")
        print("-----------")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("-----------")
        print(f" {board[6]} | {board[7]} | {board[8]} \n")
    except TypeError:
        print('game over')
display_board(['1','2','3','4','5','6','7','8','9'])

def input_board():
    test_board = ['1','2','3','4','5','6','7','8','9']
    chance = 1

    while chance < 10:
        try:
            if chance%2!=0:
                y = int(input("X's turn to play select position:"))
                while test_board[int(y)-1]=='X' or test_board[int(y)-1]=='O':
                    print(f"{y} is already taken")
                    y=int(input("X's turn to play select position:"))
                chance+=1
                test_board[int(y)-1] = 'X'
                display_board(test_board)
            else:
                y = int(input("O's turn to play select position:"))
                while test_board[int(y)-1]=='X' or test_board[int(y)-1]=='O':
                    print(f"{y} is already taken")
                    y=int(input("0's turn to play select position:"))
                chance+=1
                test_board[int(y)-1] = 'O'
                display_board(test_board)
            if (test_board[0]==test_board[1]==test_board[2] or
                    test_board[3]==test_board[4]==test_board[5] or
                    test_board[6]==test_board[7]==test_board[8] or
                    test_board[0]==test_board[3]==test_board[6] or
                    test_board[1]==test_board[4]==test_board[7] or
                    test_board[2]==test_board[5]==test_board[8] or
                    test_board[0]==test_board[4]==test_board[8] or
                    test_board[2]==test_board[4]==test_board[6]):
                if chance%2!=0:
                    print("'O' has won game over")
                    return True
                else:
                    print("'X' has won game over")
                    return True
        except IndexError,ValueError:
            print('enter a number in the range 1 - 9')
            continue

    else:
        print('its a draw')



display_board(input_board())