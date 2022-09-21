from  BJ_class import *
from BJ_functions import *

# player chips 
player_chips = Chips()

while True:
	# welcome game message
	print("WELCOME TO THE GAME OF BLACK JACK!!")

	# new deck 
	deck = Deck()
	deck.shuffle()

	# player cards
	player_hand = Hand()
	player_hand.add_cards(deck.deal())
	player_hand.add_cards(deck.deal())

	# dealer cards
	dealer_hand = Hand()
	dealer_hand.add_cards(deck.deal())
	dealer_hand.add_cards(deck.deal())

	

	#player bet 
	take_bet(player_chips)

	# show cards(where dealer's 1 card is hidden)
	show_some(player_hand,dealer_hand)

	# loop to start the game 
	while playing:

		#hit or stand for player
		hit_or_stand(deck,player_hand)

		# show cards(where dealer's 1 card is hidden)
		show_some(player_hand,dealer_hand)

		#player busts
		if player_hand.value > 21:
			player_bust(player_chips)
			break


		# when value donot exceed 21 
	if player_hand.value <= 21:

		while dealer_hand.value < 17:
				hit(deck,dealer_hand)

		#show all the cards 
		show_all(player_hand,dealer_hand)

		# dealer bust
		if dealer_hand.value > 21:
			dealer_bust(player_chips)
		# dealer win 
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_chips)
		# player win
		elif dealer_hand.value < player_hand.value:
			player_wins(player_chips)
		else:
			push()

	print(f"\n Player Total Winnings stands at: {player_chips.total}")

	# Ask player if they want to continue to play
	check = input("Do you want to play again? 'yes' or 'no': ").lower()

	if check[0].startswith('y'):

		continue
	elif check[0].startswith('n'):
		print("Thank you for playing!!")
		break



