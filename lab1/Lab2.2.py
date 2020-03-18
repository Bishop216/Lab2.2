import numpy as np
import random
import math
import matplotlib.pyplot as plt

n = 12
w = 2700
N = 64

num = w / (n - 1)

_w = []
for t in range(n):
    _w.append(w - t * num)

H = []
for i in range(N):
    H.append(0)


for t in range(n):
    A = random.choice([i for i in range(-100, 100) if i != 0])
    Phi = random.randint(-100, 100)
    for e in range(N):
        H[e] += A * math.sin(_w[t] * e + Phi)

plt.figure(figsize=(20, 15))
plt.plot(H)
plt.grid(True)
plt.show()

w_k = np.zeros(shape=(N // 2, N // 2))
for i in range(N // 2):
    for t in range(N // 2):
        w_k[i][t] = math.cos(4 * math.pi / N * i * t) + math.sin(4 * math.pi / N * i * t)

w_k_pN = np.zeros(N)
for i in range(N):
    w_k_pN[i] = math.cos(2 * math.pi / N * i) + math.sin(2 * math.pi / N * i)

f1 = np.zeros(N // 2)

f2 = np.zeros(N // 2)

f = np.zeros(N)

for i in range(N // 2):
    for t in range(N // 2):
        f2[i] += H[2 * t] * w_k[i][t]

        f1[i] += H[2 * t + 1] * w_k[i][t]

for t in range(N):
    if t < (N // 2):
        f[t] += f2[t] + w_k_pN[t] * f1[t]
    else:
        f[t] += f2[t - (N // 2)] - w_k_pN[t] * f1[t - (N // 2)]

plt.figure(figsize=(20, 15))
plt.plot(f)
plt.grid(True)
plt.show()
