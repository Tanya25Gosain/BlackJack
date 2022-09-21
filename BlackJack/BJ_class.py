import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

playing = True

class Cards:

	# defining the cards
	def __init__(self, suit,rank):
		self.suit = suit
		self.rank = rank
	# string for the card to be displayed
	def __str__(self):
		 return self.rank + " of " + self.suit


class Deck:

	# adding the cards in the string 
	def __init__(self):
		# empty deck to add cards 
		self.deck = []
		# loops for adding the cards according to the suits and ranks in the global 
		for suit in suits:
			for rank in ranks:
				# appended the cards in the string 
				self.deck.append(Cards(suit,rank))

	# displaying the string of the cards in deck 
	def __str__(self):
		# taking a empty string 
		deck_comp = ''
		# adding the string of the card in the deck 
		for card in self.deck:
			deck_comp += '\n'+ card.__str__()
		return "The Deck are:" +deck_comp

	def shuffle(self):
		# shuffling the deck 
		random.shuffle(self.deck)

	def deal(self):
		# adding the single card 
		# using pop to extract the first card from deck 
		single_card = self.deck.pop()
		return single_card



class Hand:

	# the card, value and ace to be used marked as instance
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	# adding a card and checking for ace 
	def add_cards (self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == "Ace":
			self.aces +=1

	def adjust_for_ace(self):
		if self.value >21 and self.aces:
			self.value -=10
			self.aces -=1


class Chips:

	def __init__(self):

		self.total = 100
		self.bet = 0

	def win_chips(self):
		self.total += self.bet
	
	def lose_chips(self):
		self.total -= self.bet


		

