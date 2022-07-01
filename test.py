import time

s = time.time()
tot = 0

for i in range(1, 10000001):
    tot += i

e = time.time()
print(tot, f'{e-s}s')
