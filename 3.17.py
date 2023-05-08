import random
print('input T>> ', end='')
T = int(input())
print('input t>> ', end='')
t = int(input())
cnt = 0
cnt_good = 0
for repeat in range(1000000):
    cnt += 1
    t1 = random.uniform(0, T)
    t2 = random.uniform(0, T)
    if abs(t2-t1) <= t:
        cnt_good += 1
print(cnt_good/cnt)
