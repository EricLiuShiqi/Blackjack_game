from random import *
deck = []
suits = "Clubs,Hearts,Spades,Diamonds".split(",")
values = "2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace".split(",")
def newDeck():
	global deck
	deck = []
	for i in suits:
		for j in values:
			deck.append(j + " of " + i)
newDeck()
def drawCard():
	value = choice(deck)
	deck.remove(value)
	return value
def valueofhand(cards):
    global acecount
    totalvalue=0
    acecount=0
    for i in cards:
        x=i.split()[0]
        if x=="Jack" or x=="Queen" or x=="King":
            totalvalue+=10
        elif x=="Ace":
            totalvalue+=11
            acecount+=1
        else:
            totalvalue+=int(x)
    return totalvalue
def playagain():
    decide=input("Input yes or no if you want play again or not.")
    if decide.lower()=="no":
        print("That's the end of the game. Welcome to come back.")
    elif decide.lower()=="yes":
        global deck
        newDeck()
        shuffle(deck) # I still wonder why we should use the random.shuffle(list)
        playprogram()
    else:
        playagain()
def lost():
    print("Booo, you lost.")
    playagain()
def won():
    print("Terrific, you won.") # I write the congratulation sentence same if the player won(no matter player got 21 or not). I just print the different congratulation sentence if the player got the blackjack.
    playagain()
def computersolo():
    global summ2,ace2,cardsofcomputer
    if summ2<16:
        b=drawCard()
        cardsofcomputer.append(b)
        summ2=valueofhand(cardsofcomputer)
        ace2+=acecount
        if summ2>21:
            if ace2>0:
                ace2-=1
                summ2-=10
                computersolo()
            else:
                print("The computer has number",summ2)
                won()
        elif summ2<16:
                computersolo()
        elif 16<=summ2<=21:
                if summ2>summ1:
                        print("The computer has number",summ2)
                        lost()
                elif summ2<summ1:
                        print("The computer has number",summ2)
                        won()
                else:
                        print("The computer has number",summ2)
                        print("Draw")
                        playagain()
    elif 16<=summ2<=21:
        if summ2>summ1:
            print("The computer has number",summ2)
            lost()
        elif summ2<summ1:
            print("The computer has number",summ2)
            won()
        else:
            print("The computer has number",summ2)
            print("Draw")
            playagain()
    else:
        print("The computer has number",summ2)
        won()
def goon():
    stayorhit=input("Please input Stay or Hit to draw a card or not.")
    global summ2,summ1,ace1,ace2,cardsofcomputer,cardsofplayer
    if stayorhit.lower()=="stay":
        computersolo()
    elif stayorhit.lower()=="hit":
        a=drawCard()
        cardsofplayer.append(a)
        summ1=valueofhand(cardsofplayer)
        ace1+=acecount
        if summ1>21:
            if ace1>0:
                ace1-=1
                summ1-=10
        print("Your next card is",a,".","The sum of your cards are",summ1)
        if summ1>21:
            print("The computer has number",summ2)
            lost()
        elif summ1==21:  # I regard that if the player got 21, no matter whether the computer will got 21, the winner is the player.
            print("The computer has number",summ2)
            won()
        else:
            goon()     
    else:
        goon()
def playprogram():
    global summ1,summ2,ace1,ace2,cardsofplayer,cardsofcomputer
    card1,card2,Card1,Card2=drawCard(),drawCard(),drawCard(),drawCard()
    cardsofplayer=[card1,card2]
    summ1=valueofhand(cardsofplayer)
    ace1=acecount
    cardsofcomputer=[Card1,Card2]
    summ2=valueofhand(cardsofcomputer)
    ace2=acecount
    print("Welcome to Blackjack, your first two cards are",card1,"and",card2,".","The sum of your cards are",summ1)
    if summ1==21:  # I regard that if both the computer and player got a blackjack, then the winner is the player.
        print("Congratulation, you got a blackjack.")
        playagain()
    elif summ1!=21 and summ2==21:
        print("Booo, the computer got a blackjack, you lost.")
        playagain()
    else:
        goon()
playprogram() 
