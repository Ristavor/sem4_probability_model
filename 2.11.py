import random
cnt = 0
cnt_good = 0
k = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for repeat in range(1000000):
    cnt += 1
    k_copy = list() + k
    s = ''
    while len(k_copy) > 0:
        i = random.randint(0, len(k_copy) - 1)
        s += k_copy[i]
        k_copy.remove(k_copy[i])
    if 'ABC' in s or 'ACB' in s or 'BAC' in s or 'BCA' in s or 'CAB' in s or 'CBA' in s:
        cnt_good += 1
print(cnt_good/cnt)