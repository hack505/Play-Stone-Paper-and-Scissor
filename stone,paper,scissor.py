import random

# for user input
print("""
Stone   -> 0
Paper   -> 1
Scissor -> 2""")


def bot():
    user_choice = input(">")  # to get user choice of wish
    bot_choice = random.randrange(0, 3)
    wrong = False

    if len(user_choice) == 1:
        user_choice = int(user_choice)
    else:
        print("--choice should be 0 or 1 or 2 only--")
        print("Try again!")
        exit()

    if user_choice > 2:
        wrong = True
        print("--choice should be 0 or 1 or 2 only--")
        print(" ")

    #     Logic
    case_1 = {'won': 0, 'loss': 0}  # draw
    case_2 = {'won': 1, 'loss': 0}  # paper
    case_3 = {'won': 0, 'loss': 2}  # stone

    case_4 = {'won': 1, 'loss': 0}  # paper
    case_5 = {'won': 1, 'loss': 1}  # draw
    case_6 = {'won': 2, 'loss': 1}  # scissor

    case_7 = {'won': 0, 'loss': 2}  # stone
    case_8 = {'won': 2, 'loss': 1}  # scissor
    case_9 = {'won': 2, 'loss': 2}  # draw

    #  only user win's in this all 9 case
    if case_1['won'] == user_choice and case_1['loss'] == bot_choice:
        won = 'draw'

    elif case_2['won'] == user_choice and case_2['loss'] == bot_choice:
        won = 'user'

    elif case_3['won'] == user_choice and case_3['loss'] == bot_choice:
        won = 'user'

    elif case_4['won'] == user_choice and case_4['loss'] == bot_choice:
        won = 'user'

    elif case_5['won'] == user_choice and case_5['loss'] == bot_choice:
        won = 'draw'

    elif case_6['won'] == user_choice and case_6['loss'] == bot_choice:
        won = 'user'

    elif case_7['won'] == user_choice and case_7['loss'] == bot_choice:
        won = 'user'

    elif case_8['won'] == user_choice and case_8['loss'] == bot_choice:
        won = 'user'

    elif case_9['won'] == user_choice and case_9['loss'] == bot_choice:
        won = 'draw'

    # if those 9 case is not applied than the bot will always win
    else:
        won = 'bot'

    # number in words for final result
    words = {0: 'STONE', 1: 'PAPER', 2: 'SCISSOR'}

    # final result
    print("User choice: " + f"{words.get(user_choice)}")
    print("Bot  choice: " + f"{words[bot_choice]}")
    print("--------W I N--------")

    # for wrong number choice
    if wrong:
        won = 'Draw'

    print(f"         {won}")


# for continues game play
while True:
    bot()

# by kamesh who written this code Thank you!