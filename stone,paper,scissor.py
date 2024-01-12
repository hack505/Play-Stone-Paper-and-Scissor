import json
import random

# for user input
print("""
Stone   -> 0
Paper   -> 1
Scissor -> 2""")


def bot():
    global user_choice

    try:
        user_choice_str = input(">")  # to get user choice of wish

        if len(user_choice_str) != 1:
            raise ValueError("Choice should be a single character.")

        user_choice = int(user_choice_str)

        if user_choice < 0 or user_choice > 2:
            raise ValueError("Choice should be between 0 and 2.")

    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Try again!")
        return

    bot_choice = ai(user_choice)
    wrong = False

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
    print("Bot  choice: " + f"{words.get(bot_choice)}")
    print("--------W I N--------")

    # for wrong number choice
    if wrong:
        won = 'Draw'

    print(f"         {won}")

    # increment user's choice by 1 in the JSON file
    adder(user_choice)


def adder(user_choice):
    try:
        # Read the JSON file
        with open('data.json', 'r') as files:
            data = json.load(files)

            if user_choice == 0:
                data['rock'] += 1
            elif user_choice == 1:
                data['paper'] += 1
            elif user_choice == 2:
                data['scissor'] += 1

        # Write the updated JSON data to the file
        with open('data.json', 'w') as file:
            file.write(json.dumps(data, indent=4))

    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def ai(user_choice_here):
    try:
        # load json file into a python object
        with open('data.json', 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    rock = int(data.get("rock"))
    paper = int(data.get("paper"))
    scissor = int(data.get("scissor"))

    data = [rock, paper, scissor]
    sample_space = rock + paper + scissor

    output = []

    for x in range(len(data)):
        # probabilty = favorable / sample_space
        probability = float(data[x]) / sample_space
        # then we will store in list to compare the highest
        output.append(probability)

    max_probability = max(output)

    for i, probability in enumerate(output):
        if probability == max_probability:
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 2
            else:
                return f"{random.randrange(3)}"

    try:
        adder(bot.user_choice)
    except Exception as e:
        print(f"Unexpected error: {e}")


# for continues game play
while True:
    bot()

# by kamesh who written this code Thank you!
