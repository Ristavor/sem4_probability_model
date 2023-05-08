import numpy as np
sigma = 0.2
d = 3
y_ = 2
r = 1
cnt = 0

for i in range(1000000):
    mistakeX = np.random.normal(loc=sigma, scale=d, size=1)
    mistakeY = np.random.normal(loc=sigma, scale=0, size=1)
    if mistakeX ** 2 + mistakeY ** 2 <= r ** 2:
        cnt += 1
print(cnt / i)
