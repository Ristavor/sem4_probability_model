import random
import math
cnt = 0
def F(x):
    return (1/2)*math.atan(x)+(1/2)
for i in range(1000000):
    chance = random.uniform(-100000000,100000000)
    if -1 < F(chance) < 1:
        cnt += 1
print(cnt/i)
