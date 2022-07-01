import numpy as np
import random
import pygame

pygame.init()

HEIGHT = 700
WIDTH = 700

nums = ['A']
nums += [str(i) for i in range(2, 11)]
nums += ['J', "Q", 'K']

suites = ['club', 'diamond', 'hearts', 'spades']
suite = {
    'c': 'club',
    'd': 'diamond',
    'h': 'hearts',
    's': 'spades'
}

cards = []

for i in range(len(suites)*len(nums)):
    nval = i % len(nums)
    sname = i//len(nums)
    cards.append([nums[nval], suites[sname]])

deck = cards.copy()

cards = np.array(cards)
np.random.shuffle(cards)
cards = np.ndarray.tolist(cards)

first = random.randint(0, 3)

player1 = []
player2 = []
player3 = []
player4 = []

players = [player1, player2, player3, player4]

players = players[first:] + players[:first+1]
trump = None

for i in range(len(cards)):
    players[i % 4].append(cards[i])
    while len(players[0]) == 5 and len(players[1]) != 5:
        print(players[0])
        trump = input('Please enter the Trump suite(C, S, H, D): ')
        found = False
        for j in suites:
            if trump.lower() == j[0]:
                found = True
                break
        if found:
            break
        print('Invalid Selection, Please Try again')

turn = 0
t1 = 0
t2 = 0
fsuite = 'S'
order = 'cdhs'
prio = deck[order.index(trump.lower())*len(nums)][::-1]


def val(x, prio):
    if suite[x[1]] == prio[0][1]:
        return nums.index(x[0]) + 14
    elif len(prio) > 13 and suite[x[1]] == prio[13][1]:
        return nums.index(x[0]) + 1
    else:
        return 0


while True:
    turn = []
    prio2 = prio.copy()
    win = [0, 0]
    for i in range(4):
        print(f'Player {i + 1}\'s chance')
        print(players[i])
        x = input('To play a card type nums followed by suite: ')
        if i == 0:
            fsuite = x[1]
        x = list(x)
        x[1] = x[1].lower()
        if not x[0].isdigit():
            x[0] = x[0].upper()
        if fsuite.lower() != trump.lower():
            prio2 += deck[order.index(fsuite.lower())*len(nums)][::-1]
        win[1] = max(win[1], val(x, prio2))
        if win[1] == val(x, prio2):
            win[0] = i
        del players[i][players[i].index([x[0], suite[x[1].lower()]])]
        turn.append(x)

    if win[0] % 2 == 0:
        t1 += 1
    else:
        t2 += 1

    print(f'{t1} - {t2}')

    if t1 == 7 or t1 == 7:
        break
