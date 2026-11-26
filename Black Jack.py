import random

# Card values
cards = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}

def deal_card():
    return random.choice(list(cards.keys()))

def hand_value(hand):
    value = sum(cards[card] for card in hand)

    # Adjust aces if bust
    aces = hand.count("A")
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def display_hands(player_hand, dealer_hand, hide_dealer=True):
    print("\nDealer's Hand:")
    if hide_dealer:
        print(f"{dealer_hand[0]} ?")
    else:
        print(" ".join(dealer_hand), f"({hand_value(dealer_hand)})")

    print("\nYour Hand:")
    print(" ".join(player_hand), f"({hand_value(player_hand)})")

money_remaining = 100

print("=== BLACKJACK ===")

while money_remaining > 0:
    print(f"\nmoney_remaining: ${money_remaining}")

    try:
        bet = int(input("Enter bet (0 to quit): $"))
    except ValueError:
        continue

    if bet == 0:
        break

    if bet > money_remaining or bet <= 0:
        print("Invalid bet.")
        continue

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Player turn
    while True:
        display_hands(player_hand, dealer_hand)

        player_score = hand_value(player_hand)

        if player_score > 21:
            print("\nBust! You lose.")
            money_remaining -= bet
            break

        choice = input("\nHit or Stand? (h/s): ").lower()

        if choice == "h":
            player_hand.append(deal_card())
        elif choice == "s":
            break

    # Skip dealer if player busts
    if hand_value(player_hand) > 21:
        continue

    # Dealer turn
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    display_hands(player_hand, dealer_hand, hide_dealer=False)

    print("\nResult:")

    if dealer_score > 21:
        print("Dealer busts! You win.")
        money_remaining += bet

    elif player_score > dealer_score:
        print("You win!")
        money_remaining += bet

    elif dealer_score > player_score:
        print("Dealer wins.")
        money_remaining -= bet

    else:
        print("Push (tie).")

print(f"\nGame over. Final Money: ${money_remaining}")
