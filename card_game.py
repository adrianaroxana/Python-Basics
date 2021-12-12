# Go fish!

import random
import os


class Player:
    def __init__(self, name, playerset, pairs):
        self.name = name
        self.playerset = playerset
        self.pairs = pairs

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


def create_deck():
    Deck = []
    Kings = ["J", "Q", "K"]
    for i in range(4):
        for j in range(1, 11):
            Deck.append(j)
        for x in range(len(Kings)):
            Deck.append(Kings[x])
    return Deck


def sort_set(playerset):
    playerset = list(
        map(int, filter(lambda x: x.isdigit(), sorted(map(str, playerset))))
    ) + list(filter(lambda x: x.isalpha(), sorted(map(str, playerset))))
    return playerset


def check_pairs(player, playerset):
    try:
        for i in range(len(playerset)):
            if playerset[i] == playerset[i + 1] == playerset[i + 2] == playerset[i + 3]:
                player.playerset.remove(playerset[i])
                player.playerset.remove(playerset[i + 1])
                player.playerset.remove(playerset[i + 2])
                player.playerset.remove(playerset[i + 3])

                player.pairs += 1

    except Exception:
        return player.pairs


def print_winner(player1, player2):
    if player1.pairs > player2.pairs:
        print(player1.getName(), "won! He has", player1.pairs, "pairs.")
    elif player2.pairs < player1.pairs:
        print(player2.getName(), "won! He has", player2.pairs, "pairs.")
    else:
        print("It's a tie!")


def play_game():
    Deck = create_deck()

    random.shuffle(Deck)
    player1 = Player("", [], 0)
    player2 = Player("", [], 0)
    p1 = input("Player1, please enter your name: ")
    player1.setName(p1)
    p2 = input("Player2, please enter your name: ")
    player2.setName(p2)

    for i in range(5):
        player1.playerset.append(Deck[i])
        Deck.remove(Deck[i])

    for i in range(5):
        player2.playerset.append(Deck[i])
        Deck.remove(Deck[i])

    print("Initial deck: ", Deck)

    player = 1

    while len(Deck) > 0:
        os.system("cls")
        if player == 1:
            print()
            print("It's", player1.getName(), "'s turn!")
            print(player1.getName(), "set of cards: ", sort_set(player1.playerset))

            requiredCard = input("I need this card: ")
            try:
                r = int(requiredCard)
                if r in player2.playerset:
                    player1.playerset.append(r)
                    player2.playerset.remove(r)
                else:
                    print("Go fish!")
                    c = random.randint(0, len(Deck) - 1)
                    player1.playerset.append(Deck[c])
                    Deck.remove(Deck[c])

            except ValueError:
                if requiredCard in player2.playerset:
                    player1.playerset.append(requiredCard)
                    player2.playerset.remove(requiredCard)
                else:
                    print("Go fish!")
                    c = random.randint(0, len(Deck) - 1)
                    player1.playerset.append(Deck[c])
                    Deck.remove(Deck[c])

            player = 2
            check_pairs(player1, sort_set(player1.playerset))

            print(player1.getName(), "set of cards: ", sort_set(player1.playerset))
            print("Pairs of ", player1.getName(), ": ", player1.pairs)

        else:
            os.system("cls")
            print()
            print("It's", player2.getName(), "'s turn!")
            print(player2.getName(), "set of cards: ", sort_set(player2.playerset))
            requiredCard = input("I need this card: ")
            try:
                r = int(requiredCard)
                if r in player1.playerset:
                    player2.playerset.append(r)
                    player1.playerset.remove(r)
                else:
                    print("Go fish!")
                    c = random.randint(0, len(Deck) - 1)
                    player2.playerset.append(Deck[c])
                    Deck.remove(Deck[c])

            except ValueError:
                if requiredCard in player1.playerset:
                    player2.playerset.append(requiredCard)
                    player1.playerset.remove(requiredCard)
                else:
                    print("Go fish!")
                    c = random.randint(0, len(Deck) - 1)
                    player2.playerset.append(Deck[c])
                    Deck.remove(Deck[c])

            player = 1
            check_pairs(player2, sort_set(player2.playerset))
            print(player2.getName(), "set of cards: ", sort_set(player2.playerset))
            print("Pairs of ", player2.getName(), ": ", player2.pairs)
    print_winner(player1, player2)


play_game()
