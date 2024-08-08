cards = ['A']
cards.extend([str(i) for i in range(2, 11)])
cards.extend(['J', 'Q', 'K'])
deck = []

for c in ['S', 'H', 'D', 'C']:
    deck.extend([c + i for i in cards])