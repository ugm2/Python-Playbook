import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    # Added. Marks the hierarchy suits order
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # Added. Private rank card method for sorting
    def _rank_card(self, card):
        rank_value = self.ranks.index(card.rank)
        return rank_value * (len(self.suit_values)) + self.suit_values[card.suit]

    # Added. Sorts deck in a defined way
    def sort_deck(self):
        return sorted(self._cards, key=self._rank_card)
