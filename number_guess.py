import random
number_to_be_guessed = random.randint(1,100)
guess_count = 10

while guess_count > 0:
    x = int(input("Enter a Number: "))
    if number_to_be_guessed == x:
        print("You have guessed the correct number.")
        break
    elif number_to_be_guessed < x:
        print("the number u have entered is greater")
        guess_count = guess_count - 1
    elif number_to_be_guessed > x:
        print("the number u have entered is smaller")
        guess_count = guess_count - 1

if guess_count <= 0:
    print("You ran out of guess\n")
    print("Game Over....\n")
    print("new line")