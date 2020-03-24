import random

current_try = 1
random_num = random.randint(1, 20)

while current_try != 11:
    if int(input(f"Try number: {current_try}, Enter you guess from 1 to 20: ")) == random_num:
        print("Congrats!! You guess the random number right!")
        break
    current_try += 1
else:
    print("Sorry you couldn't guess it")
