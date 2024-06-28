def get_number_from_player(player):
    while True:
        try:
            number = int(input(f"{player}, please enter your number: "))
            if number <= 0:
                print("Please enter a positive integer.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")

def guess_number(player, number):
    start_time = time.time()
    attempts = 0
    while True:
        try:
            guess = int(input(f"{player}, please guess the number: "))
            attempts += 1
            if guess == number:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
            else:
                hint = [digit for digit in str(guess) if digit in str(number)]
                print(f"Hint: Digits in your guess present in the number are: {' '.join(hint)}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    end_time = time.time()
    return end_time - start_time

def play_game():
    print("Player 1 will give the number and Player 2 will guess it. Then they will switch roles.")
    number_p1 = get_number_from_player("Player 1")
    time_p2 = guess_number("Player 2", number_p1)
    print(f"Player 2 guessed the number in {time_p2:.2f} seconds.\n")
    
    # Player 2 gives the number, Player 1 guesses
    number_p2 = get_number_from_player("Player 2")
    time_p1 = guess_number("Player 1", number_p2)
    print(f"Player 1 guessed the number in {time_p1:.2f} seconds.\n")
    
    # Determine the winner
    if time_p1 < time_p2:
        print(f"Player 1 wins! Guessed the number faster in {time_p1:.2f} seconds.")
    elif time_p2 < time_p1:
        print(f"Player 2 wins! Guessed the number faster in {time_p2:.2f} seconds.")
    else:
        print("It's a tie! Both players took the same amount of time.")
