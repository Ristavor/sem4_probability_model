import random
k = 5
p_k = [0.5, 0.4, 0.5, 0.2, 0.3]
cnt = 0
for i in range(1000000):
    for j in range(k):
        if p_k[j] >= random.uniform(0, 1):
            cnt += 1
print(cnt / i)
