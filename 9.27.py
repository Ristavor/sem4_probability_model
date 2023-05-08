import random
cnt = 0
for i in range(1000000):
    voices = [0, 0, 0]
    for n in range(3):
        for k in range(3):
            chance = random.uniform(0, 1)
            if chance <= 0.5:
                voices[k] += 1
    voices.sort()
    if voices[2] >= 2 and voices[2] != voices[1]:
        cnt += 1
print(cnt / i)