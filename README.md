# BlackJack Simulator
A BlackJack simulator to play any number of hands using different strategies

## The Rules
To keep the code relatively simple, a lot of the rules are hard-coded. This simulator assumes:
* Dealer hits soft-17
* Player can double-down any first 2 cards
* Player can split any number of times
* Blackjack pays 6:5 (1.2)
* Surrender is allowed and the loss is 1/2

## The Structure
### Overview
The way this code is structured is:
* That the game is played at a Table.
* A Table has 1 Shoe of cards. The Shoe can have anywhere from 1 to 10 Decks of cards.
* A Table has 1 Dealer.
* A Table has 1 or more Players.
* A Player has 1 or more Hands. Generally, a player has 1 hand unless there are splits, in which case player can have multiple hands.
* A Dealer has 1 hand.

To simulate a round of BlackJack, you simply:
1. Create a Table object (which creates a dealer and shoe with 8 decks by default)
1. Add a player to tha table
1. And then you call Table.playRound to play 1 round of BlackJack.
1. The table then needs to reset using the Table.reset() method to play another hand.

The results of each hand is stored in the hand itself.

### Code to simulate 1,000 rounds
The code to simulate 1,000 rounds of BlackJack can be as simple as:
```
table = Table()
table.players.append(Player())
for i in range(0, 1000):        # Simulates 1,000 rounds of BlackJack
    table.playRound()
    table.reset()
```
In order to see the results, including dealer's FaceCard and the decision the player made, you can also use the Table.printShortResults() or Table.printVerboseResults(). Here is an example of printing condensed results:
```
table = Table()

table.players.append(Player())
print("Round, Dealer FaceCard, Player Card 1, Card 2, Total, Soft Hand, Is BlackJack, Busted, Action, Result, Value")

for i in range(0, 1000):        # Simulates 1,000 rounds of BlackJack
    table.playRound()
    print(str(i) + ", " + table.printShortResults())
    table.reset()
```

The results include a "Value" for the hand that ranges from -2.0 to 2.0:
* -1.0 Means a normal loss for a hand
* +1.0 Means a normal win for a hand
* -2.0 Means a Double-Downed round was lost
* +2.0 Means a Double-Downed round was won
* +1.2 Means a BlackJack win
* -0.5 Means a loss by surrender

## The Classes

### The Shoe
The Shoe is designed to be extremely simple. When its initialized (or shuffled), it simply creates an array of 52 x [Num of Decks] elements numbered from 1 to 52. When a card is needed from the Shoe via getCard(), the Shoe randomly picks an array element and removes it from the array and returns it as the card. However, prior to returning the card, it first does a "% 13" operation to simulate a card from 1 (Ace) to 13 (King), and since in BlackJack, a 10, Jack, Queen and King are all 10s, if the card is >= 10, it returns a 10.

### The Hand
A lot of the logic on how to play a hand is in the Hand class.

The Hand class has 3 main methods on how the hand will be played:
* basicStrategyPlay - This plays using standard BlackJack basic strategy.
* randomPlay - This plays using a random allowed action. Results of this could be used to train machine learning alogrithms.
* dealerPlay - This plays using standard BlackJack dealer play strategy.

The getHandTotal() method is also useful to get the hand total, which takes into consideration soft hands (where an Ace is counted as an 11). If a hand total is considered to be a soft hand, it also sets the "softHand" variable that's passed in to true.

### The Player and Dealer classes
Since most of the logic for how the hand is played is actually in the Hand class, the Player and Dealer objects are just wrappers to hold a hand. Ideally, it might make sense to refactor the code to put the "play" methods into the Player and Dealer classes rather than the Hand class.

Another potential refactor might make the Dealer a kind of Player rather than its own class.

### The Table class
The Table class is where the bulk of the action is.

When the table "playRound()" is called, the table first deals the first 2 cards as no logic is needed prior to dealing the first 2 cards to all players and the dealer. If the dealer doesn't have a BlackJack, it then continues the play.

The playPlayerHand() is probably the most complicated part of the code because in the event of a Split, it can also be called recursively. The code is written so that the playPlayerHand() uses the basicStrategyPlay() method to play the round. You can also change this to randomPlay() to see what would happen if the player plays the game by taking a random action based on available actions.
