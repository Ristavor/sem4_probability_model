import random
cnt = 0
for i in range(100000):
    M = 5
    Tn = 10
    A = 40
    N0 = 1000
    num_atoms = M * N0 / A
    cnt_death = 0
    theory = 0.6931471806 / Tn
    for j in range(int(num_atoms)):
        chance = random.uniform(0, 1)
        if chance <= theory:
            cnt_death += 1
    cnt += cnt_death
print(cnt / i)
