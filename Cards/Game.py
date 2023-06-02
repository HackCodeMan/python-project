from Module_Cards import *
import time
import random
class Creator(object):
    """creator (Create objects)"""
    @staticmethod
    def create_list_hands(other_players) -> tuple[list[Hand], Hand]:
        hands: list[Hand] = []
        my_hand: Hand = Hand()
        hands.append(my_hand)
        for i in range(other_players):
            hands.append(Hand())
        return hands , my_hand
    @staticmethod
    def create_deck() -> Deck:
        deck: Deck = Deck()
        deck.populate()
        deck.shuffle()
        return deck
    @staticmethod
    def create_trump_card(deck) -> Card:
        trump_card: Card = random.choice(deck.cards)
        deck.remove(trump_card)
        return  trump_card
def instruction():
    """display rules of the game"""
    print("Инструкция по игре 'Переводной Дурак'(Жмите Enter,чтобы продолжить):")
    input("\t-Перед началом игры перемешивается колода карт. (Делает программа)")
    input("\t-Затем раздается игрокам(Роботу/ам и вам) по 6 карт. (Делает программа)")
    input("\t-Определяется козырь карты случайно (Делает программа)")
    input("\t-Этим козырем можно бить любые масти кроме козырных с любыми значениями.\n"
          "\tПримечание: Козырем нельзя побить другой козырь с большим значением")
    input("\t-Игру начинает человек, имеющий на руках козырную карту наименьшего значения."
          "\n\t-Ходят, играя в дурака, всегда по часовой стрелке, то есть на сидящего слева игрока.")
    input("\t-Цель Игры: Избавиться От Карт")
    input("\t-Игрок, который ходит, выбрасывает карту или карты(если значение их одинаковое),"
          "\nа игрок, который защищается, должен покрыть.")
    input("\t-Покрыть карту возможно тогда и только тогда, когда значение твоей карты больше,\n"
          "И масть одинаковая,\n"
          "Или если карта противника не козырь, можешь бить любым своим козырем")
    input("-Конец")
    pass
def display_cards_table_move(my_hand,table):
    print(f"Ход")
    print(f"Стол: {table}")
    print(f"Твои карты: {my_hand}")
def player_choose_card() -> Card:
    rank = ""
    suit = ""
    card_defined = False
    while not card_defined:
        card = input("Ваша карта: ")
        while rank not in Card.RANKS:
            for symbol in card:
                if symbol in Card.RANKS:
                    rank = symbol
                else:
                    print("Не распознал карту. Введите ещё раз")
                    continue
            if suit in Card.SUITS:
                suit = suit
            else:
                print("Не распознал карту. Введите ещё раз")
                continue
            card_defined = True
    return Card(rank, suit)
def main():
    """Main program"""
    print("Добро пожаловать в карточную игру 'Дурак'")
    time.sleep(1)
    print("Вам предлагается пройтись по правилам игры.")
    time.sleep(1)
    def y_or_n(question: str) -> str:
        """Ask with answer 'Y' or 'N' """
        answer_y_or_n: None = None
        while "N" != answer_y_or_n != "Y":
            print(question)
            answer_y_or_n: str = input("Ваш выбор(Y\\N): ").upper()
        return answer_y_or_n
    answer: str = y_or_n("Хотите ознакомиться с правилами?")
    if answer == "Y":
        instruction()
    hands, my_hand = Creator.create_list_hands(2)
    deck1: Deck = Creator.create_deck()
    table1: Hand = Hand()
    deck1.deal(hands = hands)
    trump_card: Card = Creator.create_trump_card(deck1)
    print(f"Козырная карта:  {trump_card}")
    player_move = random.choice((True,False))
    while deck1 != 0 or (len(my_hand) != 0 and len(hands[1]) != 0):
        if player_move:
            print(f"Твои карты: {my_hand}")
            print("Выбери какой картой ты хочешь сходить?")
            choose_card = " "
            list_str_cards = []
            item = 0
            for card in my_hand.cards:
                list_str_cards.append(str(card))
            while choose_card not in list_str_cards:
                choose_card = input("Ваш выбор: ")
                if choose_card not in list_str_cards:
                    print("Нет этой карты!")
                    continue
                else:
                    item = list_str_cards.index(choose_card)
            my_hand.give(my_hand[item], table1)
            display_cards_table_move(my_hand,table1)
main()
