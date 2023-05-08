import random
cnt = 0
for i in range(1000000):
    material = random.uniform(0, 1)
    first = random.uniform(0, 1)
    if material <= 0.09:
        if first <= 0.2:
            cnt += 1
    elif material <= 0.25:
        if first <= 0.3:
            cnt += 1
    elif material <= 0.50:
        if first <= 0.4:
            cnt += 1
    elif material <= 0.75:
        if first <= 0.4:
            cnt += 1
    elif material <= 0.91:
        if first <= 0.3:
            cnt += 1
    elif material <= 1:
        if first <= 0.2:
            cnt += 1
print(cnt/i)