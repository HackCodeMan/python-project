# This module have a lot of classes related to cards
# Module's User will be able to make a lot of Card games
# Write in your project in different line 'import Module_Cards' and will start to use
# Code:

# Import modules
import sys
import random

# Class Exception:
class RankErrors(Exception):
    """Exception wrong Rank"""
    def __init__(self,fun_name: str = "Your Function or Class"):
        print(fun_name, ": does not work correctly!!")
        self.text: str = ": No such Rank exist!!"
        print(self.__class__.__name__ + self.text)
        sys.exit()
class SuitError(Exception):
    """Exception wrong Suit"""
    def __init__(self,fun_name: str = "Your Function or Class"):
        print(fun_name, ": does not work correctly!!")
        self.text: str = ": No such Suit exist!!"
        print(self.__class__.__name__+ self.text)
        sys.exit()
class NotElementsError(Exception):
    def __init__(self,fun_name: str = "Your Function or Class"):
        print(fun_name,": does not work correctly!!")
        self.text: str = ": There is not elements!!"
        print(self.__class__.__name__+ self.text)
        sys.exit()

# Class objects
class Card:
    """Virtual Card"""
    RANKS: tuple[str] = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
    SUITS: tuple[str] = ("d","c","h","s")
    def __init__(self, rank: str, suit: str):
        """Will work when initialized a new object ."""
        if rank in Card.RANKS:
            self.rank: str = rank
        else:
            raise RankErrors(self.__class__.__name__)
        if suit in Card.SUITS:
            self.suit: str = suit
        else:
            raise SuitError(self.__class__.__name__)
    def __str__(self) -> str:
        """Will work when used the function str() or print().
           Type: string"""
        return self.rank + self.suit
    def __int__(self) -> int:
        """The Card Rank from str to int"""
        if self.rank == "A":
            int_rank: int = 14
        elif self.rank == "K":
            int_rank: int = 13
        elif self.rank == "Q":
            int_rank: int = 12
        elif self.rank == "J":
            int_rank: int = 11
        elif self.rank in ("2","3","4","5","6","7","8","9","10"):
            int_rank: int = int(self.rank)
        else:
            raise RankErrors
        return int_rank

class Unprintable_card(Card):
    """Virtual Unprintable card, cannot be printed"""
    def __str__(self):
        """Will work when used the function str() or print().
           Type: string"""
        return "<Нельзя распечатать>"
class Positionable_Card(Card):
    """Virtual card, you can turn face up or down"""
    def __init__(self, rank: str, suit: str, face_up: bool):
        """Will work when initialized a new object ."""
        super().__init__(rank,suit)
        self.face_up = face_up
    def __str__(self) -> str:
        """Will work when used the function str() or print().
           Type: string"""
        if self.face_up:
            rep: str = super().__str__()
        else:
            rep: str = "XX"
        return rep
    def flip(self):
        """Flip the Positionable Card"""
        self.face_up = not self.face_up
class Hand:
    """Virtual Hand with cards"""
    def __init__(self):
        """Will work when initialized a new object ."""
        self.cards: list[Card] = []
    def __str__(self) -> str:
        """Will work when used the function str() or print().
           Type: string"""
        rep: str = "<Пусто>"
        if self.cards:
            rep: str = ""
            symbols_in_line: int = 0
            for card in self.cards:
                rep += str(card) + " "
                symbols_in_line += 1
                if symbols_in_line == 12:
                    rep += "\n"
                    symbols_in_line = 0
        return rep
    def __getitem__(self, item):
        """Returns a card by its index"""
        return self.cards[item]
    def __len__(self) -> int:
        """Will work when used the function len().
           Type: integer"""
        return len(self.cards)
    def __bool__(self) -> bool:
        """Will work when used the function bool(). Return True or False.
           Type: string"""
        return bool(self.cards)
    def remove(self,card: Card):
        """Remove the card"""
        self.cards.remove(card)
    def add(self, card: Card):
        """Add the card in hand"""
        self.cards.append(card)
    def give(self,card: Card, other_hand):
        """Gave the card other hand"""
        self.cards.remove(card)
        other_hand.add(card)
    def clear(self):
        """Clear all cards in Hand"""
        self.cards.clear()
class Deck(Hand):
    """Virtual Deck of Cards"""
    def populate(self):
        """Add all cards in Deck"""
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.add(Card(rank = rank, suit = suit))
    def shuffle(self):
        """Shuffling the Deck"""
        if self.cards:
            random.shuffle(self.cards)
        else:
            raise NotElementsError(self.__class__.__name__)
    def deal(self,hands: list[Hand], per_hands: int = 6):
        """Deal the cards all players"""
        if self.cards:
            for hand in hands:
                for i in range(per_hands):
                    card = random.choice(self.cards)
                    self.cards.remove(card)
                    hand.add(card)
        else:
            raise NotElementsError(self.__class__.__name__)

if __name__ == "__main__":
    print("Это модуль!! Его надо запускать не напрямую,"
          "а импортировать в ваш проект и использовать его!!")
    pass