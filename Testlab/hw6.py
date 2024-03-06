import numpy as np

k1 = 0.1   
k2 = 0.2
t_start = 0
t_end = 1
step_size = 0.1

A = 2
B = 0

A_values = [A]
B_values = [B]

for t in np.arange(t_start, t_end, step_size):
    dA = -k1 * A + k2 * B
    dB = k1 * A - k2 * B
    A = A + dA * step_size
    B = B + dB * step_size
    A_values.append(A)
    B_values.append(B)

for i, (a,b) in enumerate(zip(A_values, B_values)):
    print(f"step{i}: A = {a:.3f}, B = {b:.3f}")