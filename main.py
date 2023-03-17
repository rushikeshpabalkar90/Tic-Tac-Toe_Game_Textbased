import random
import time

print("!! Welcome to Tic Tac Toe Game !!")

# ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = f"\n| {ls[6]} | {ls[7]} | {ls[8]} |\n_____________\n| {ls[3]} | {ls[4]} | {ls[5]} |\n_____________\n| {ls[0]} | {ls[1]} | {ls[2]} |\n"

print(
    f"\n| {ls[6]} | {ls[7]} | {ls[8]} |\n_____________\n| {ls[3]} | {ls[4]} | {ls[5]} |\n_____________\n| {ls[0]} | {ls[1]} | {ls[2]} |\n")

computer_choice = "o"
game_on = True

user_choice = ""

while user_choice != "o" and user_choice != "x":
    user_choice = input("Choose what you want x/o? : ").lower()

if user_choice == "o":
    computer_choice = "x"

print(f"user choice : {user_choice} and computer choice : {computer_choice}")


while game_on:
    with open("winner.txt") as file:
        first = file.read()

    com_choose = True
    user_choose = True

    if first == "0":
        while user_choose:
            board_number = int(input("Enter the number between 1-9 showing in board: "))
            if board_number in ls:
                ls[board_number - 1] = user_choice
                user_choose = False
        print(
            f"\n| {ls[6]} | {ls[7]} | {ls[8]} |\n_____________\n| {ls[3]} | {ls[4]} | {ls[5]} |\n_____________\n| {ls[0]} | {ls[1]} | {ls[2]} |\n")

        time.sleep(0.9)
        with open("winner.txt", "w") as file:
            file.write("1")

    if first == "1":
        print("\ncomputer's move... ")

        while com_choose:
            random_num = random.randint(1, 10)
            if random_num in ls:
                ls[random_num - 1] = computer_choice
                com_choose = False

            if 1 not in ls and 2 not in ls and 3 not in ls and 4 not in ls and 5 not in ls and 6 not in ls and 7 not in ls and 8 not in ls and 9 not in ls:
                print("\n!!It's Draw Play again!!")
                game_on = False
                com_choose = False

        print(
            f"\n| {ls[6]} | {ls[7]} | {ls[8]} |\n_____________\n| {ls[3]} | {ls[4]} | {ls[5]} |\n_____________\n| {ls[0]} | {ls[1]} | {ls[2]} |\n")
        with open("winner.txt", "w") as file:
            file.write("0")

    if ls[0] == ls[1] == ls[2] == user_choice or ls[3] == ls[4] == ls[5] == user_choice or \
            ls[6] == ls[7] == ls[8] == user_choice or ls[0] == ls[3] == ls[6] == user_choice or \
            ls[1] == ls[4] == ls[7] == user_choice or ls[2] == ls[5] == ls[8] == user_choice or \
            ls[0] == ls[4] == ls[8] == user_choice or ls[2] == ls[4] == ls[6] == user_choice:
        print("user win!!")
        with open("winner.txt", "w") as file:
            file.write("0")

        game_on = False

    elif ls[0] == ls[1] == ls[2] == computer_choice or ls[3] == ls[4] == ls[5] == computer_choice or \
            ls[6] == ls[7] == ls[8] == computer_choice or ls[0] == ls[3] == ls[6] == computer_choice or \
            ls[1] == ls[4] == ls[7] == computer_choice or ls[2] == ls[5] == ls[8] == computer_choice or \
            ls[0] == ls[4] == ls[8] == computer_choice or ls[2] == ls[4] == ls[6] == computer_choice:
        print("computer win!!")
        with open("winner.txt", "w") as file:
            file.write("1")
        game_on = False
