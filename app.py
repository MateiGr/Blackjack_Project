import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

first_user_cards = random.sample(cards, 2)
first_dealer_cards = random.sample(cards, 1)

print(f"Your first cards are : {first_user_cards}")
print(f"The dealer's first card is : {first_dealer_cards}")

hit = False

def blackJack() :
    while hit == False :
        user_input = input("Do you want to draw a card? (y for yes) : ")
        if user_input == "y":
            next_user_card = random.choice(cards)
            print(f"Your next card is : {next_user_card}")
            first_user_cards.append(next_user_card)
            if sum(first_user_cards) > 21 :
                if 11 in first_user_cards :
                    print("You were over 21, but had an eleven, we substracted the eleven.")
                    first_user_cards[first_user_cards.index(11)] = 1
                    print(f"Your cards are : {first_user_cards}")
                else :
                    print(f"You are over 21, you lose.")
                    return
            else :
                print(f"Your cards are : {first_user_cards}")
        else :
            hit == True
            second_dealer_card = random.choice(cards)
            first_dealer_cards.append(second_dealer_card)
            if sum(first_dealer_cards) < 17 :
                print(f"The dealer's cards are : {first_dealer_cards}")
                print("The dealers sum is under 17, they pick another card")
                third_dealer_card = random.choice(cards)
                first_dealer_cards.append(third_dealer_card)
                print(f"The dealer's cards are : {first_dealer_cards}")

            if sum(first_dealer_cards) > 21 :
                if 11 in first_dealer_cards:
                    print("They were over 21, but had an eleven, we substracted the eleven.")
                    first_user_cards[first_dealer_cards.index(11)] = 1
                    print(f"Their cards are : {first_dealer_cards}")
                else:
                    print(f"They are over 21, they lose.")
                    return
            else :
                print(f"The dealer's cards are : {first_dealer_cards}")

            print(" ")
            print(f"Your sum is {sum(first_user_cards)}")
            print(f"The dealer's sum is {sum(first_dealer_cards)}")

            if sum(first_user_cards) < sum(first_dealer_cards) :
                print("You lose")
            elif sum(first_user_cards) == sum(first_dealer_cards):
                print("Draw")
            else :
                print("You win")

            return

blackJack()