import random
while True:
    print("Welcome to the Guessing Game!")
    a = int(input("Enter the lower bound: "))
    b = int(input("Enter the upper bound: "))
    num = random.randint(a, b)
    attempts = 0
    while True:
        guess = int(input(f"Guess a number between {a} and {b}: "))
        attempts += 1
        if guess < a or guess > b:
            print("Please choose a number within the given range.")
        elif guess == num:
            print(f"Congratulations! You've guessed the correct number {num} in {attempts} attempts.")
            break
        elif guess > num:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing! Goodbye!")
        break
            