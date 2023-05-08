import random

# Задаем радиусы внутреннего и внешнего кругов
k = 10
n = 50

# Количество испытаний
num_trials = 10**6

# Счетчик количества раз, когда было только одно попадание в круг радиуса k
num_hits = 0

# Генерация случайных точек и проверка попадания
for i in range(num_trials):
    x1 = random.uniform(-n, n)
    x2 = random.uniform(-n, n)
    y1 = random.uniform(-1, 1) * (n ** 2 - x1 ** 2) ** 0.5
    y2 = random.uniform(-1, 1) * (n ** 2 - x2 ** 2) ** 0.5
    r1 = (x1**2 + y1**2)**0.5
    r2 = (x2**2 + y2**2)**0.5
    if r1 <= k and r2 > k or r1 > k and r2 <= k:
        num_hits += 1

# Вычисление вероятности одного попадания в круг радиуса k
probability = num_hits / num_trials

print(probability)
