"""
Lines of Action main class
Starbuck Beagley
"""

import argparse #parser
import Player
import random
import Board
import Move
import Display
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("computer_player", help="-c if computer opponent is desired")
    args = parser.parse_args()

    computer_player = False

    if args.computer_player and args.computer_player == "c":
        computer_player = True

    rows = 8
    cols = 8
    player1 = Player.Player(1, 'x')
    player2 = Player.Player(2, 'o')
    board = Board.Board(rows, cols, player1, player2)
    board.reset_board()
    move = Move.Move(board, player1, player2)
    display = Display.Display(rows, cols)
    current_player = player1

    print("")

    while 1:
        display.show_board(board.get_grid())

        if move.check_for_win(player1) or move.check_for_win(player2):
            print("\n\(*o*)/\(*o*)/\(*o*)/ " + str(current_player) + " wins! \(*o*)/\(*o*)/\(*o*)/\n")
            break

        if computer_player and current_player == player2:
            print("\n**Computer's move**\n")
            time.sleep(1.5)
            a = get_computer_move(player2, move)

        else:
            print("\n**" + str(current_player) + "'s move**")
            user_in = input("Enter piece and destination coordinates, row before column, separated by a space: ")
            print("")

            if user_in.lower() == "q":
                break

            l = list("".join(user_in.split()))

            a = []

            if len(l) != 4 or not translate(l, a):
                time.sleep(1)
                print("(v_v) Please enter valid coordinates (v_v)\n")
                continue

        result = move.make_move(current_player, a[0], a[1], a[2], a[3])

        if result[0] == 0:
            print("(v_v) " + result[1] + " (v_v)\n")
        elif result[0] == 1:
            if computer_player and current_player == player2:
                print("(^u^) " + result[1][0:6] + "Computer" + result[1][14:] + " (^u^)\n")
                time.sleep(1.5)
            else:
                print("(^u^) " + result[1] + " (^u^)\n")
                time.sleep(1.5)
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1


def get_computer_move(player, move):
    r1 = random.randint(0, 7)
    c1 = random.randint(0, 7)
    r2 = random.randint(0, 7)
    c2 = random.randint(0, 7)
    while 1:
        if move.legal_move(player, r1, c1, r2, c2) == "Legal":
            a = [r1, c1, r2, c2]
            return a
        else:
            return get_computer_move(player, move)


def translate(l, a):
    try:
        i = int(l[0])
        a.append(i)
    except ValueError:
        return False
    if l[1].lower() == 'a':
        a.append(0)
    elif l[1].lower() == 'b':
        a.append(1)
    elif l[1].lower() == 'c':
        a.append(2)
    elif l[1].lower() == 'd':
        a.append(3)
    elif l[1].lower() == 'e':
        a.append(4)
    elif l[1].lower() == 'f':
        a.append(5)
    elif l[1].lower() == 'g':
        a.append(6)
    elif l[1].lower() == 'h':
        a.append(7)
    else:
        return False
    try:
        i = int(l[2])
        a.append(i)
    except ValueError:
        return False
    if l[3].lower() == 'a':
        a.append(0)
    elif l[3].lower() == 'b':
        a.append(1)
    elif l[3].lower() == 'c':
        a.append(2)
    elif l[3].lower() == 'd':
        a.append(3)
    elif l[3].lower() == 'e':
        a.append(4)
    elif l[3].lower() == 'f':
        a.append(5)
    elif l[3].lower() == 'g':
        a.append(6)
    elif l[3].lower() == 'h':
        a.append(7)
    else:
        return False
    return True

if __name__ == "__main__":
    main()