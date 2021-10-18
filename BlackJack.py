import random
from enum import Enum, auto

class PlayOptions(Enum):
    STAY = 1
    HIT = 2
    DOUBLE = 3
    SURRENDER = 5
    SPLIT = 4

class DealerResults(Enum):
    BLACKJACK = 1
    BUSTED = 2
    STAY = 3

class HandType(Enum):
    NORMAL = 1
    SPLIT = 2
    DOUBLE = 3

class HandResults(Enum):
    WIN = auto()
    DOUBLEWIN = auto()
    DOUBLELOSS = auto()
    BLACKJACK = auto()
    LOST = auto()
    PUSH = auto()
    SURRENDER = auto()

# Define the matricies for basic strategy
hardHand2CardLookup = [
    # columns are based on dealer's face card from 1 (Ace) to 10, rows based on player's total (no ace) 5 to 21
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT]
    ,[PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.SURRENDER, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.SURRENDER]
    ,[PlayOptions.SURRENDER, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.SURRENDER, PlayOptions.SURRENDER]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
]
hardHandLookup = [
    # columns are based on dealer's face card from 1 (Ace) to 10, rows based on player's total (no ace) 5 to 21
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
]
softHand2CardLookup = [
    # columns are based on dealer's face card from 1 (Ace) to 10, rows based on player's total with at least 1 ace counted as 11, totals of 14 to 21
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
]
softHandLookup = [
    # columns are based on dealer's face card from 1 (Ace) to 10, rows based on player's total with at least 1 ace counted as 11, totals of 14 to 21
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
]
pairHandLookup = [
    # columns are based on dealer's face card from 1 (Ace) to 10, rows based on player's pair card, 1 through 10
    [PlayOptions.SURRENDER, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT]
    ,[PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT]
    ,[PlayOptions.SURRENDER, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT]
    ,[PlayOptions.STAY, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.STAY, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.STAY]
    ,[PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY]
]


class Shoe:
    def __init__(self, d = 1) -> None:
        self.cards = []
        self.decks = d
        if (self.decks <= 0) or (self.decks > 10):
            self.decks = 1

        for i in range(0, 52*self.decks):
            self.cards.append(i%52+1)

    def getCard(self):
        card = self.cards.pop(random.randrange(len(self.cards))) % 13 + 1
        if card > 10:
            card = 10
        return card

    def needShuffle(self):
        # Return true if less than 1/3 of the shoe is remaining
        return (len(self.cards) / (self.decks*52)) < .33

    def shuffle(self):
        self.__init__(self.decks)

class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.total = 0
        self.actions = []
        self.handType = HandType.NORMAL
        self.result = None
    
    def addCard(self, card):
        self.cards.append(card)

    def getHandTotal(self, softHand = False):
        self.total = 0
        for card in self.cards:
            if card >= 10:
                self.total += 10
            elif card > 1:
                self.total += card
            else:                       # card is an ace
                if self.total <= 10:    # if total <= 10, count the ace as an 11, and set softHand
                    softHand = True
                    self.total += 11
                else:                   # if total > 10, must count ace as a 1
                    self.total += 1
        
        if self.total > 21 and softHand:   # if total > 21 and we have aces counting as 11...
            self.total -= 10
            softHand = False
        
        return self.total

    def basicStrategyPlay(self, dealerFaceCard):
        softHand = False
        handTotal = self.getHandTotal(softHand)

        if len(self.cards) < 2:
            return PlayOptions.HIT
        elif handTotal > 21:
            self.actions.append(PlayOptions.STAY)
            return PlayOptions.STAY
        elif len(self.cards) == 2:
            if self.cards[0] == self.cards[1]:
                # use pair hand lookup
                self.actions.append(pairHandLookup[self.cards[0]-1][dealerFaceCard-1])
                return pairHandLookup[self.cards[0]-1][dealerFaceCard-1]
            
            elif softHand:
                # Use the soft hand table since there's an ace counted as 11
                self.actions.append(softHand2CardLookup[handTotal-13][dealerFaceCard-1])
                return softHand2CardLookup[handTotal-13][dealerFaceCard-1]
            
            else:
                # Use the hand hand lookup table since everything else is a hard hand
                self.actions.append(hardHand2CardLookup[handTotal-5][dealerFaceCard-1])
                return hardHand2CardLookup[handTotal-5][dealerFaceCard-1]
        else:
            # Hand has more than 2 cards
            if softHand:
                # Use the soft hand table since there's an ace counted as 11
                self.actions.append(softHandLookup[handTotal-13][dealerFaceCard-1])
                return softHandLookup[handTotal-13][dealerFaceCard-1]
            
            else:
                # Use the hand hand lookup table since everything else is a hard hand
                self.actions.append(hardHandLookup[handTotal-5][dealerFaceCard-1])
                return hardHandLookup[handTotal-5][dealerFaceCard-1]

    def randomPlay(self):           # Returns a random allowable action

        # First, let's make sure the hand has at least 2 cards in it
        # This action is NOT recorded as first 2 cards are not player's choice
        if len(self.cards) < 2:
            return PlayOptions.HIT
        
        if len(self.cards) == 2:                    # First 2 cards, we might have different options
            if self.getHandTotal() == 21:           # Player has blackjack
                self.actions.append(PlayOptions.STAY)
                return PlayOptions.STAY

            elif self.cards[0] == self.cards[1]:      # Two of the same cards
                action = random.choice(list(PlayOptions))     # Randomly select action based on all available actions
                self.actions.append(action)
                return action
            
            else:
                action = random.choice([PlayOptions.HIT, PlayOptions.STAY, PlayOptions.DOUBLE, PlayOptions.SURRENDER])
                self.actions.append(action)
                return action

        if self.getHandTotal() < 21:                # randomly play something unless we have 21
            action = random.choice([PlayOptions.HIT, PlayOptions.STAY])
            self.actions.append(action)
            return action
        else:
            self.actions.append(PlayOptions.STAY)
            return PlayOptions.STAY

    def dealerPlay(self):               # Returns an action based on using BJ dealer rules
        # Assumes dealer has already received at least 2 cards

        softHand = False
        handTotal = self.getHandTotal(softHand)
        if len(self.cards) == 2 and handTotal == 21:  # Dealer has blackjack
            return PlayOptions.STAY
        
        if handTotal < 17 or (handTotal == 17 and softHand): # Hit until we have 17, also hit on soft-17
            return PlayOptions.HIT
        
        return PlayOptions.STAY
            
    def isBlackJack(self):
        return (len(self.cards) == 2) and (self.getHandTotal() == 21)

    def reset(self):
        self.__init__()

class Player:
    def __init__(self) -> None:
        self.hands = []
        self.hands.append(Hand())         # Start player with 1 hand
    
    def reset(self):
        self.__init__()

class Dealer:
    def __init__(self) -> None:
        self.hand = Hand()

    def reset(self):
        self.__init__()

class Table:
    def __init__(self) -> None:
        self.shoe = Shoe(8)     #Table's shoe has 8 decks
        self.players = []
        self.dealer = Dealer()

    def dealFirstTwoCards(self):
        # First, give each player a card, then the dealer
        for p in self.players:
            p.hands[0].addCard(self.shoe.getCard())
        
        # Dealer's first card
        self.dealer.hand.addCard(self.shoe.getCard())

        # Give each player their 2nd card
        for p in self.players:
            p.hands[0].addCard(self.shoe.getCard())

        # Dealer's 2nd card
        self.dealer.hand.addCard(self.shoe.getCard())

    def playRound(self):
        self.activeHands = len(self.players)     # Set active hands to the number of players

        # check to see if shoe needs to be shuffled
        if self.shoe.needShuffle():
            self.shoe.shuffle()

        self.dealFirstTwoCards()

        # Players play their hands if dealer doesn't have blackjack
        if not self.dealer.hand.isBlackJack():
            # Have each player play their hand
            for i in range (0, len(self.players)):
                p = self.players[i]
                self.playPlayerHand(p.hands[0], p, self.dealer.hand.cards[0])

            # If there are any active hands left, then dealer plays
            if self.activeHands > 0:
                while True:
                    dealerChoice = self.dealer.hand.dealerPlay()
                    if dealerChoice == PlayOptions.STAY:
                        break

                    if dealerChoice == PlayOptions.HIT:
                        self.dealer.hand.addCard(self.shoe.getCard())
        
        self.recordHandResults()
            
    def playPlayerHand(self, hand, player, dealerFaceCard):
        if hand.isBlackJack():
            # This hand has won and doesn't need to continue
            self.activeHands -= 1
            return                  
        else:
            while True:
                playerChoice = hand.basicStrategyPlay(dealerFaceCard)

                if playerChoice in [PlayOptions.HIT, PlayOptions.DOUBLE]: 
                    hand.addCard(self.shoe.getCard())
                
                if playerChoice == PlayOptions.SPLIT:
                    self.activeHands += 1                      # New active hand as a result of split
                    newHand = Hand()
                    newHand.handType = HandType.SPLIT          # Recording hand type in case of different rules for split hands
                    hand.handType = HandType.SPLIT
                    newHand.cards.append(hand.cards.pop(0))    # Remove a card from old hand to create new hand
                    player.hands.append(newHand)
                    self.playPlayerHand(newHand, player, dealerFaceCard)

                if playerChoice in [PlayOptions.STAY, PlayOptions.DOUBLE, PlayOptions.SURRENDER]:
                    break

            if playerChoice == PlayOptions.DOUBLE:
                hand.handType = HandType.DOUBLE 
            elif playerChoice == PlayOptions.SURRENDER:
                # Player busted, active player count decreases
                self.activeHands -= 1
                hand.result = HandResults.SURRENDER
            elif hand.getHandTotal() > 21:
                # Player busted, active player count decreases
                self.activeHands -= 1
                if hand.handType == HandType.DOUBLE:
                    hand.result = HandResults.DOUBLELOSS
                else:
                    hand.result = HandResults.LOST

    def recordHandResults(self):
        # Go through each hand to see if it has won
        for i in range (0, len(self.players)):
            p = self.players[i]
            for j in range (0, len(p.hands)):
                h = p.hands[j]
                # Check to see if hand already has a result (because of surrender or bust)
                if h.result == None:
                    # Check for dealer blackjack
                    if self.dealer.hand.isBlackJack():
                        if h.isBlackJack():
                            h.result = HandResults.PUSH
                        else:
                            h.result = HandResults.LOST
                    # Check for hand blackjack (must be normal hand, not a split, and dealer must not have blackjack)
                    elif h.isBlackJack() and h.handType == HandType.NORMAL:
                        h.result = HandResults.BLACKJACK
                    # Check if player has busted (should already be checked when player is playing, but just in case)
                    elif h.getHandTotal() > 21:
                        if h.handType == HandType.DOUBLE:
                            h.result = HandResults.DOUBLELOSS
                        else:
                            h.result = HandResults.LOST
                    # Check if dealer has busted
                    elif self.dealer.hand.getHandTotal() > 21:
                        # dealer has busted, all hands win
                        if h.handType == HandType.DOUBLE:
                            h.result = HandResults.DOUBLEWIN
                        else:
                            h.result = HandResults.WIN
                    # Check for push
                    elif self.dealer.hand.getHandTotal() == h.getHandTotal():
                        h.result = HandResults.PUSH
                    # Player has better hand
                    elif h.getHandTotal() > self.dealer.hand.getHandTotal():
                        if h.handType == HandType.DOUBLE:
                            h.result = HandResults.DOUBLEWIN
                        else:
                            h.result = HandResults.WIN
                    # Dealer has better hand
                    else: #self.dealer.hand.getHandTotal() > h.getHandTotal():
                        if h.handType == HandType.DOUBLE:
                            h.result = HandResults.DOUBLELOSS
                        else:
                            h.result = HandResults.LOST     

    def printVerboseResults(self):
        result = "Dealer FaceCard = " + str(self.dealer.hand.cards[0])
        result += ", Total = " + str(self.dealer.hand.getHandTotal())
        result += ", BJ = " + str(self.dealer.hand.isBlackJack())
        result += ", Bust = " + str(self.dealer.hand.getHandTotal() > 21)
        result += ", Cards = " + str(self.dealer.hand.cards)
        
        for i in range (0, len(self.players)):
            p = self.players[i]
            result += ", Player " + str(i+1)
            for j in range (0, len(p.hands)):
                h = p.hands[j]
                result += ", Hand " + str(j+1)
                result += ", Total = " + str(h.getHandTotal())
                result += ", BJ = " + str(h.getHandTotal() == 21 and len(h.cards) == 2)
                result += ", Bust = " + str(h.getHandTotal() > 21)
                result += ", Cards = " + str(h.cards)
                result += ", Actions = " + str(h.actions)
                result += ", " + str(h.result)

        return result

    def printShortResults(self):
        result = str(self.dealer.hand.cards[0])
        
        for i in range (0, len(self.players)):
            p = self.players[i]
            for j in range (0, 1): # Only doing first hand
                h = p.hands[j]
                result += ", " + str(h.cards[0]) + ", " + str(h.cards[1])
                firstTwoCards = h.cards[0] + h.cards[1]
                softHand = False
                if h.cards[0] == 1 or h.cards[1] == 1:
                    firstTwoCards += 10
                    softHand = True
                result += ", " + str(firstTwoCards)
                result += ", " + str(softHand)                                      # Has an ace
                result += ", " + str(h.getHandTotal() == 21 and len(h.cards) == 2)  # Is blackjack
                result += ", " + str(h.getHandTotal() > 21)                         # Busted
                if len(h.actions) > 0:
                    result += ", " + str(h.actions[0])
                else:
                    result += ", NO ACTION"

                result += ", " + str(h.result)
                
                # Calculate value of hand based on results
                value = 0.0
                if h.result == HandResults.WIN:
                    value = 1.0
                elif h.result == HandResults.DOUBLEWIN:
                    value = 2.0
                elif h.result == HandResults.DOUBLELOSS:
                    value = -2.0
                elif h.result == HandResults.BLACKJACK:
                    value = 1.2     # Based on 6:5 blackjack return. Change to 1.5 for 3:1
                elif h.result == HandResults.LOST:
                    value = -1.0
                elif h.result == HandResults.PUSH:
                    value = 0.0
                elif h.result == HandResults.SURRENDER:
                    value = -0.5

                result += ", " + str(value)
        return result
    
    def reset(self):
        for player in self.players:
            player.reset()
        
        self.dealer.reset()

        if self.shoe.needShuffle():
            self.shoe.shuffle()


table = Table()

table.players.append(Player())
print("Round, Dealer FaceCard, Player Card 1, Card 2, Total, Soft Hand, Is BlackJack, Busted, Action, Result, Value")

for i in range(0, 1000):        # Simulates 1,000 rounds of BlackJack
    table.playRound()
    print(str(i) + ", " + table.printShortResults())
#    print("Round " + str(i) + ": " + table.printVerboseResults())     # More verbose printout of each hand played
#    print("\n")

    table.reset()
