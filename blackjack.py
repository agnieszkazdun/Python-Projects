import random


def play_the_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = []
    computer_cards = []
    def deal_card(whose_hand):
        whose_hand.append(random.choice(cards))




    # CALCULATING SCORES

    def calculate_score(list_of_cards):
        the_score = sum(list_of_cards)
        ace = 11
        if len(list_of_cards) == 2 and the_score == 21:
            return 0 #Blackjack
        elif the_score > 21 and ace in list_of_cards:
            list_of_cards.remove(ace)
            list_of_cards.append(1)
            return sum(list_of_cards)
        else:
            return the_score

    # Deal initial cards
    deal_card(user_cards)
    deal_card(user_cards)
    deal_card(computer_cards)
    deal_card(computer_cards)

    # Calculate user's score
    user_score = calculate_score(user_cards)

    # Show user's hand and computer's first card
    print(f"Your hand: {user_cards}, your score: {user_score}  \nComputer's first card: {computer_cards[0]}")


    if user_score == 0:
        print("Blackjack! You win!")
    else:
        while user_score < 21:
            draw = input("Type 'y' to draw or 'n' to stand.").lower()
            if draw == "y":
                deal_card(user_cards)
                user_score = calculate_score(user_cards)
                print(f"Your new hand: {user_cards}, your score: {user_score}")
            elif draw == 'n':
                print("You chose to stand.")
                break


    # Computer's turn to draw cards if it's score is less than 17
    computer_score = calculate_score(computer_cards)

    while computer_score < 17:
        deal_card(computer_cards)
        computer_score = calculate_score(computer_cards)


    # Reveal both hands and compare scores

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")

    # Determine winner

    if user_score > 21:
        print("You went over, you lose.")
    elif computer_score > 21:
        print("Computer went over you win.")
    elif user_score > computer_score:
        print("You win!")
    elif computer_score > user_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play Blackjack? 'y' or 'n'")
    if play_again == "y":
        play_the_game()
    else:
        print("Thanks for playing! Bye!")




play_the_game()

