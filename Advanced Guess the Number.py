import random
import time

def playagain():
    if input("Do you want to play again? (YES/NO)").lower() == "yes":
        startgame()

def startgame():
    game_status = True

    number_of_tries = int(input("How many tries do you want to give yourself? "))
    current_try = 1
    
    num2 = int(input("What range do you want your number to be, from 1 to {number2}? (ANSWER: number2)"))
    print("Generating number..")
    time.sleep(1)
    
    number = random.randint(1, num2)
    
    while (current_try != number_of_tries + 1) and (game_status == True):
        answer = input(f"Try number: {current_try}, Please enter your guess of a number between 1 and {num2} \n")

        if answer.isdigit() == False:
            print(f"{answer} is not a number, Please try again!")
            time.sleep(1)
            continue
        if int(answer) == number:
            print("Congrats!! You got it right!!!!!")
            game_status = False
            time.sleep(2)
            playagain()
        elif int(answer) not in range(1, num2+1):
            print(f"{answer} is not in range of 1 and {num2}")
            continue
        else:
            current_try += 1
            continue
    if current_try == number_of_tries:
        print("Sorry you couldn't guess it")
        playagain()

startgame()
