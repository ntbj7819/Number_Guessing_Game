import random
import statistics

# Global variable to store the high score (fewest guesses)
high_score = float('inf')  # Start with infinity, so any number of guesses will be better

def start_game():
    global high_score  # Access the global high_score variable
    guesses = []  # Reset guesses for each new game
    print("\nWelcome to the guessing game!")
    
    # Display the current high score
    if high_score == float('inf'):
        print("There's no high score yet. Try to beat the record!")
    else:
        print(f"The current high score is {high_score} guesses. Try to beat it!")

    solution = random.randint(1, 50)

    while True:
        try:
            guess = int(input("Please enter a number from 1 to 50: "))
            if guess < 1 or guess > 50:
                print("Please choose a number between 1 and 50.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        guesses.append(guess)

        if guess > solution:
            print("It's lower.")
        elif guess < solution:
            print("It's higher.")
        else:
            print("You guessed correctly!")
            break

    # Game stats
    num_guesses = len(guesses)
    print(f"\nIt took you {num_guesses} chances to guess correctly!")
    print(f"Mean of guesses: {round(statistics.mean(guesses))}")
    print(f"Median of guesses: {statistics.median(guesses)}")

    try:
        print(f"Mode of guesses: {statistics.mode(guesses)}")
    except statistics.StatisticsError:
        print("No single mode.")

    # Check if the current game has set a new high score
    if num_guesses < high_score:
        high_score = num_guesses  # Update high score
        print(f"New high score! You guessed it in {num_guesses} attempts!")

def replay():
    while True:
        answer = input("\nWould you like to continue playing? Y/N: ").lower()
        if answer == "y":
            start_game()
        elif answer == "n":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Please choose Y or N")

# Start the first game
start_game()
replay()
