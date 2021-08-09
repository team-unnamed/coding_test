import sys
input = sys.stdin.readline

n = int(input())
n_cards = list(map(int, input().rstrip('\n').split()))

m = int(input())
m_cards = list(map(int, input().rstrip('\n').split()))

cards = [0]*20000001

for n_card in n_cards:
    cards[n_card+10000000] +=1

for m_card in m_cards:
    print(cards[m_card+10000000], end= ' ') 