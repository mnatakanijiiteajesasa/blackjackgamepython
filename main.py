import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!!"
    elif user_score == 0:
        return "You have won by a black jack!"
    elif computer_score == 0:
        return "Computer has black jack. You Lose"
    elif user_score > 21:
        return "You went overboard. You Lose"
    elif computer_score > 21:
        return "Opponent went overboard. You Win"
    elif user_score == 21:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards :{user_cards}, current score: {user_score}")
        print(f"Computer's card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score == 21:
            is_game_over = True
        else:
            user_to_continue = input("Type y to continue and n to stop:\n")
            if user_to_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(compare(user_score, computer_score))


play_game()
