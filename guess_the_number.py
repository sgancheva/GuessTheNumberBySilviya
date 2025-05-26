import random

computer_number = random.randint(1, 100)

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    player_input = input(f"This is your {attempts + 1}/{max_attempts} -> -> Guess the number (1 - 100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_input = int(player_input)
    attempts += 1

    if player_input == computer_number:
        print("You guessed it!")
        break
    elif player_input > computer_number:
        print("Too high!")
    else:
        print("Too low!")

    if attempts == max_attempts:
        print(f"Sorry, you used all your attempts!The correct number is {computer_number}!")

# Level 2

if player_input == computer_number:

    computer_number_level_2 = random.randint(1, 200)

    attempts = 0
    max_attempts = 8

    while attempts < max_attempts:
        player_input = input(f"This is your {attempts + 1}/{max_attempts} -> -> Level 2: Guess the number (1 - 200): ")

        if not player_input.isdigit():
            print("Invalid input. Try again...")
            continue

        player_input = int(player_input)
        attempts += 1

        if player_input == computer_number:
            print("You guessed it!")
            break
        elif player_input > computer_number:
            print("Too high!")
        else:
            print("Too low!")

        if attempts == max_attempts:
            print(f"Sorry, you used all your attempts!The correct number is {computer_number_level_2}!")

