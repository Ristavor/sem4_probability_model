import random
repeat = 1000000
cnt = 0
for i in range(repeat):
    cntm = 0
    n = 20
    r = 10
    m = 5
    k = 3
    for j in range(r):
        get = random.randint(1, n)
        if get <= n-m:
            n -= 1
        else:
            m -= 1
            cntm += 1
    if cntm == k:
        cnt += 1
print(cnt/i)
