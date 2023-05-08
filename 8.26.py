
import random

cnt = 0
for i in range(1000000):
    cnt5 = 0
    cnt2 = 0
    chance1 = random.uniform(0, 1)
    chance2 = random.uniform(0, 1)
    chance3 = random.uniform(0, 1)
    chance4 = random.uniform(0, 1)
    chance5 = random.uniform(0, 1)
    if chance1 <= 0.7:
        cnt5 += 1
    else:
        cnt2 += 1
    if chance2 <= 0.7:
        cnt5 += 1
    else:
        cnt2 += 1
    if chance3 <= 0.7:
        cnt5 += 1
    else:
        cnt2 += 1
    if chance4 <= 0.7:
        cnt5 += 1
    else:
        cnt2 += 1
    if chance5 <= 0.7:
        cnt5 += 1
    else:
        cnt2 += 1
    if cnt5 == 5 or cnt2 >= 2:
        cnt += 1
print(cnt/i)