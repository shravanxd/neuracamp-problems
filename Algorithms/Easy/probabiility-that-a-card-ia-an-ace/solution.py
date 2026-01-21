def solution(deck):
    # Count number of aces in the deck
    ace_count = sum(1 for card in deck if card[0] == 'A')
    # Calculate probability
    probability = ace_count / len(deck)
    # Return rounded probability
    return round(probability, 2)