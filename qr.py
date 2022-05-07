import numpy as np
import math

A = np.array([
    [1,0],
    [1,1],
    [0,1],
])


print("A = ",A)

# 1. u1 = v1

v1 = np.array(A[:, 0])
v1 = v1.reshape(len(v1), 1)
u1 = v1
print("u1 = ", u1)

# 2. e1 = u1/||u1||

u1_len = 0
for i in u1:
    u1_len += i[0] ** 2
u1_len = math.sqrt(u1_len)

e1 = u1 / u1_len
print("e1 = ",e1)

# u2 = v2 - projekcjau1(v2)

v2 = np.array(A[:, 1])
v2 = v2.reshape(len(v2), 1)
projekcja = (np.transpose(v2) @ u1 / (np.transpose(u1) @ u1)) * u1
projekcja

u2 = v2 - projekcja
print("u2 = ",u2)


# e2 = u2/||u2||

u2_len = 0
for i in u2:
    u2_len += i[0] ** 2
u2_len = math.sqrt(u2_len)
print(u2_len)

e2 = u2 / u2_len
print("e2 = ",e2)

# Q = [e1 e2]

Q = np.array(e1)
Q = np.append(Q, e2, axis=1)
print("Q = ",Q)

# R = Q^TA

R = np.transpose(Q) @ A
print("R = ",R)

# A = QR

print(Q @ R)