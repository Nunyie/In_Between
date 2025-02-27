#Nunyie
#BSCpE
#Card Game "In Between"

import random

def card_value(card):
    rank = card.split(' ')[0]
    return ranks.index(rank)

def play_in_between():
    while True:
        # Shuffle the deck at the start
        random.shuffle(deck)

        player_score = 0

        while len(deck) > 2:  # Ensure there are enough cards for two to be drawn
            card1 = deck.pop()
            card2 = deck.pop()
            print(f"\nThe dealer has drawn: {card1} and {card2}")

            # Input validation for the guess
            while True:
                guess = input("Do you think the next card will be in between these two cards? (yes/no): ").strip().lower()
                if guess in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            next_card = deck.pop()
            print(f"The next card is the: {next_card}")

            is_between = (card_value(card1) < card_value(next_card) < card_value(card2)) or (card_value(card2) < card_value(next_card) < card_value(card1))
            
            if (guess == 'yes' and is_between) or (guess == 'no' and not is_between):
                print("Correct guess!")
                player_score += 1
            else:
                print("Wrong guess!")

            print(f"Current Score: {player_score}")

            # Input validation for continuing the game
            while True:
                continue_game = input("Would you like to continue playing? (yes/no): ").strip().lower()
                if continue_game in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if continue_game != 'yes':
                print("Thank you for playing!")
                print(f"Your final score is: {player_score}")  # Show final score
                return  # Exit the function to end the game

            if len(deck) > 2:
                random.shuffle(deck)
            else:
                print("Not enough cards left to continue the game.")
                break

            print(f"Final Score: {player_score}")

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',]
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

# Start the game
if __name__ == "__main__":
    print('Welcome to the Card Game "In Between"!')
    play_in_between()
