"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    lettres = ["J", "K", "Q"]
    Ass = ["A"]
    number = ["2","3","4","5","6","7","8","9","10"]

    if card not in lettres or  card not in number or card not in Ass :
        print("Donner une carte qui est dans le jeu")

    if card in lettres   :
        return 10
    elif card in Ass:
        return 1
    else:
        return int(card)

    pass


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    
    if value_one > value_two  :
        return card_one 
    elif value_two > value_one:
        return card_two

    else:
        return card_one, card_two

    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    add_values = value_one + value_two
    
    if card_one == "A" or card_two == "A" :
        return 1
        
        
    if add_values <= 10:
        return 11
    else:
        return  1
    pass


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    #Belle victoire je l'ai resolu seul
    if value_one == 1 and value_two == 10:
        return True
    elif value_one == 10 and value_two == 1:
        return True
    else:
        return False
    
    
    
    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    #Fais de moi meme belle victoire encore
    if value_one == value_two:
        return True
    elif value_two == value_one:
        return True
    else:
        return False 
        
    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    add_values = value_one + value_two
    
    # Bravo encore une fois tu vois que tu comprends quand tu veux  
    if add_values == 9:
        return True
    elif add_values == 10:
        return True
    elif add_values == 11:
        return True
    else:
        return False

    
    pass
