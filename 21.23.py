import numpy as np

n1 = 4
n2 = 3
p = 0.2
Z = 3
cnt = 0

for i in range(1000000):
    X = np.random.binomial(n1, p, 1)  # генерация выборки для первой группы
    Y = np.random.binomial(n2, p, 1)  # генерация выборки для второй группы
    if X + Y == Z:
        cnt += 1

print(cnt / 1000000)
