import random

def select_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def provide_clue(actual_number, guessed_number):
    if actual_number == guessed_number:
        return "Congratulations! You've guessed the correct number."
    elif actual_number < guessed_number:
        return "Try a smaller number."
    else:
        return "Try a greater number."

def main():
    min_range = 1  # Set the minimum range for the random number
    max_range = 100  # Set the maximum range for the random number
    actual_number = select_random_number(min_range, max_range)
    
    attempts = 0
    score = 100  # Starting score
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_range} and {max_range}.")
    
    while True:
        try:
            guessed_number = int(input("Take a guess: "))
            attempts += 1
            
            clue = provide_clue(actual_number, guessed_number)
            print(clue)
            
            if actual_number == guessed_number:
                print(f"You guessed the number in {attempts} attempts! Your final score is {score}.")
                break
            else:
                score -= 10  # Reduce the score for each incorrect guess
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
