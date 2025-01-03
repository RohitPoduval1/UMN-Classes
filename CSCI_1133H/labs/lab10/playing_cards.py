# Lab 10
# playing_cards.py



ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['C', 'S', 'D', 'H']


def rank_suit_count(cards):
    rank_count = {}
    suit_count = {}
    
    # card[0] is the rank
    # card[1] is the suit
    for card in cards:
        if (card[0] in ranks):
            if (card[0] not in rank_count.keys()): 
                rank_count[card[0]] = 1
            else:
                rank_count[card[0]] += 1
        if (card[1] in suits):
            if (card[1] not in suit_count.keys()): 
                suit_count[card[1]] = 1
            else:
                suit_count[card[1]] += 1
    
    return (rank_count, suit_count)


def main():
    print(rank_suit_count([ 'AS', 'AD', '2C', 'TH', 'TS' ]))


if __name__ == '__main__':
    main()
