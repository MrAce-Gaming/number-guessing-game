import random

def ask():
    while True:
        try:
            x = int(input("Enter an integer between 1 and 100: "))
            if x >= 1 and x <= 100:
                return x
            else:
                print("Please enter an integer between 1 and 100!")
        except ValueError:
            print("Please enter an integer between 1 and 100!")
        
number = random.randint(1, 100)
guess = 1

def number_guessing_game(number):
    print("Welcome to the Number Guessing Game!\n" \
    "I'm thinking of a number between 1 and 100.")

    while True:
        try:
            difficulty = int(input("Please select the difficulty level:\n" \
            "1. Easy (10 chances)\n" \
            "2. Medium (5 chances)\n" \
            "3. Hard (3 chances)\nEnter Choice: "))
        except ValueError:
            print("Please enter the number lined with the difficulty levels!")
        else:
            print(f"Great! Let's start the game!")
            break
    
    if difficulty == 1:
            print("Great! So you have chosen Easy difficulty.\n" \
                "You get exactly 10 chances before you lose the game.")
            user_guess = ask()

            while not user_guess == number:
                if guess == 10:
                    print("Oops! You have lost the game!\n"\
                        f"The number was {number}!\n"\
                        f"You took {guess} guess(es)!")
                    break
                elif user_guess > number:
                    print("Guess lower!")
                    user_guess = ask()
                    guess+=1
                elif user_guess < number:
                    print("Guess higher!")
                    user_guess = ask()
                    guess+=1
                elif user_guess == number:
                    print("Congratulations! You have successfully guessed the number!\n"\
                        f"The number was indeed {number}!\n"\
                        f"You took {guess} guess(es).")
    elif difficulty == 2:
            print("Great! So you have chosen Medium difficulty.\n" \
                "You get exactly 5 chances before you lose the game.")
            user_guess = ask()

            while not user_guess == number:
                if guess == 5:
                    print("Oops! You have lost the game!\n"\
                        f"The number was {number}!\n"\
                        f"You took {guess} guess(es)!")
                    break
                elif user_guess > number:
                    print("Guess lower!")
                    user_guess = ask()
                    guess+=1
                elif user_guess < number:
                    print("Guess higher!")
                    user_guess = ask()
                    guess+=1
                elif user_guess == number:
                    print("Congratulations! You have successfully guessed the number!\n"\
                        f"The number was indeed {number}!\n"\
                        f"You took {guess} guess(es).")
    elif difficulty == 3:
            print("Great! So you have chosen Hard difficulty.\n" \
                "You get exactly 3 chances before you lose the game.")
            user_guess = ask()
            
            while not user_guess == number:
                if guess == 3:
                    print("Oops! You have lost the game!\n"\
                        f"The number was {number}!\n"\
                        f"You took {guess} guess(es)!")
                    break
                elif user_guess > number:
                    print("Guess lower!")
                    user_guess = ask()
                    guess+=1
                elif user_guess < number:
                    print("Guess higher!")
                    user_guess = ask()
                    guess+=1
                elif user_guess == number:
                    print("Congratulations! You have successfully guessed the number!\n"\
                        f"The number was indeed {number}!\n"\
                        f"You took {guess} guess(es).")

while True:
    number_guessing_game(number=number)
    replay = input("Do you want to replay the game? (Y/N): ").upper()
    if replay != 'Y':
        break
