playing = True
def take_bet(chips):
	# taking chips as argument
	while True:
		try:
			# user input for bet
			chips.bet = int(input("enter the bet you want to place: "))

		except ValueError:
			#checking for error 
			print("Integer number required!!")

		else:
			#checking for exceed limi =t
			if chips.bet > chips.total:
				print("Limit Exceeded!!")
				continue
		# breaking loop
		break



def hit(deck,hand):
	# adding single card 
	hand.add_cards(deck.deal())
	# checking for ace
	hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    
    while True:
        x = input("Hit or Stand? enter h or s: ")
        
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print("Player Stand Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s")
            continue
        break

def show_some(player,dealer):
	# dealer 1st card is hidden
	print("\n Dealer's Hand:")
	print(" <hidden card> ")
	print('',dealer.cards[1])

	# player cards
	print("\nPlayer's Hand: ", *player.cards, sep='\n')


def show_all(player,dealer):
	# dealer cards and total value 
	print("\n Dealer's Hand: ", *dealer.cards, sep = '\n')
	print("Dealer's value = ", dealer.value)

	# player cards and value
	print("\n player's Hand: ", *player.cards, sep = '\n')
	print("Player's value = ", player.value)



def player_bust(chips):
	print("Player Bust!!")
	chips.lose_chips()

def player_wins(chips):
	print("Player wins!!")
	chips.win_chips()

def dealer_bust(chips):
	print("Dealer Bust!!")
	chips.win_chips()

def dealer_wins(chips):
	print("Dealer wins!!")
	chips.lose_chips()

def push():
	print("Its a TIE!!! player and dealer had the same value")




