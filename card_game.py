#!/usr/bin/env python3
import random
from typing import List, Tuple

class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value
        
    def __str__(self) -> str:
        values = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        value_str = values.get(self.value, str(self.value))
        return f"{value_str} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        # Using 2-14 for card values (14 = Ace)
        for suit in suits:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self) -> Card:
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

class WarGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_cards: List[Card] = []
        self.computer_cards: List[Card] = []
        self.deal_initial_cards()
        
    def deal_initial_cards(self):
        # Deal cards alternately to player and computer
        while len(self.deck.cards) > 0:
            self.player_cards.append(self.deck.deal())
            if len(self.deck.cards) > 0:
                self.computer_cards.append(self.deck.deal())
    
    def play_round(self) -> Tuple[str, Card, Card]:
        if not self.player_cards or not self.computer_cards:
            return None, None, None
            
        player_card = self.player_cards.pop(0)
        computer_card = self.computer_cards.pop(0)
        
        print(f"\nYour card: {player_card}")
        print(f"Computer's card: {computer_card}")
        
        if player_card.value > computer_card.value:
            self.player_cards.extend([player_card, computer_card])
            return "player", player_card, computer_card
        elif computer_card.value > player_card.value:
            self.computer_cards.extend([player_card, computer_card])
            return "computer", player_card, computer_card
        else:
            # In case of a tie, both cards go to their original owners
            self.player_cards.append(player_card)
            self.computer_cards.append(computer_card)
            return "tie", player_card, computer_card
    
    def get_scores(self) -> Tuple[int, int]:
        return len(self.player_cards), len(self.computer_cards)
    
    def game_over(self) -> bool:
        return len(self.player_cards) == 0 or len(self.computer_cards) == 0

def main():
    print("Welcome to War Card Game!")
    print("Each player draws a card, and the higher card wins the round.")
    print("The game ends when one player has all the cards.")
    
    game = WarGame()
    rounds = 0
    
    while not game.game_over() and rounds < 100:  # Limit to 100 rounds to prevent infinite games
        rounds += 1
        input("\nPress Enter to play a round...")
        
        result, player_card, computer_card = game.play_round()
        if result is None:
            break
            
        player_score, computer_score = game.get_scores()
        
        if result == "player":
            print("You win this round!")
        elif result == "computer":
            print("Computer wins this round!")
        else:
            print("It's a tie!")
            
        print(f"\nScores - You: {player_score} cards, Computer: {computer_score} cards")
    
    # Determine the winner
    player_score, computer_score = game.get_scores()
    print("\nGame Over!")
    if player_score > computer_score:
        print("Congratulations! You win!")
    elif computer_score > player_score:
        print("Computer wins! Better luck next time!")
    else:
        print("It's a tie!")
    
    print(f"\nFinal Scores:")
    print(f"You: {player_score} cards")
    print(f"Computer: {computer_score} cards")

if __name__ == "__main__":
    main() 