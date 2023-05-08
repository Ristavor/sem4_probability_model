import random
cnt1miss = 0
cnt3thmissed = 0
for i in range(1000000):
    target = 0
    chance1 = random.uniform(0,1)
    chance2 = random.uniform(0,1)
    chance3 = random.uniform(0,1)
    if chance1 <= 4/5:
        target += 1
    if chance2 <= 3/4:
        target += 1
    if chance3 <= 2/3:
        target += 1
    if target == 2 and chance3 > 2/3:
        cnt3thmissed += 1
    if target == 2:
        cnt1miss += 1
print(cnt3thmissed / cnt1miss)