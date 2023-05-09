import random

def simulate_game(m, n):
    player1_wins = 0
    player2_wins = 0
    
    while player1_wins < m and player2_wins < n:
        if random.uniform(0, 1) <= 0.5:
            player1_wins += 1
        else:
            player2_wins += 1
    
    return player1_wins == m

# пример использования
cnt1 = 0
cnt2 = 0
for i in range(1000000):
    if simulate_game(4, 3):
        cnt1 += 1
    else:
        cnt2 += 1
print((cnt1/i)/(cnt2/i))