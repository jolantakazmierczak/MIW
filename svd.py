import numpy as np
from numpy.linalg import eig
from scipy.linalg import svd
# A = U . Sigma . V^T

A = np.array([
    [1,2,0],
    [2,0,2],

])

print(A)

# transpozycja
AT = A.transpose()

print(AT)

# AA^T
AAT = A @ AT

print(AAT)

# lambda

eigenValues_AAT, eigenVectors_AAT = eig(AAT)
idx = eigenValues_AAT.argsort()[::-1]
eigenValues_AAT = eigenValues_AAT[idx]
eigenVectors_AAT = eigenVectors_AAT[:, idx]


print(eigenValues_AAT)

# print(eigenVectors_AAT)
U = eigenVectors_AAT
print("----------")
print("U:")
print(U)
print("----------")
# sigmas
sigmas = np.sqrt(eigenValues_AAT)
print(sigmas)

# Sigma
size = (len(A), len(A[0]))


Sigma = np.zeros(size)
np.fill_diagonal(Sigma, Sigma.diagonal() + sigmas)
print(Sigma)

# v1 i v2

u_1 = U[:,0]
u_2 = U[:,1]
# u_3 = U[:,2]
print(u_1)
print(u_2)
# print(u_3)

sigma_1 = np.reciprocal(sigmas[0])
v_1 = AT@u_1 * sigma_1

sigma_2 = np.reciprocal(sigmas[1])
v_2 = AT@u_2 * sigma_2

print("v1: ",v_1)
print("v2: ",v_2)

# v3

ATA = AT@A

print(ATA)

eigenvalues_ATA, eigenvectors_ATA = np.linalg.eig(ATA)
ATA_sorted = np.flip(np.argsort(eigenvalues_ATA))
eigenvectors_ATA = eigenvectors_ATA[:, ATA_sorted]
print("---")
print(eigenvalues_ATA)
print("---")
print(eigenvectors_ATA)
print("---")

v_3 = eigenvectors_ATA[:,2]
print("v3: ", v_3)
print("----------------------------------")

v_size = (len(A[0]), len(A[0]))
V  = np.zeros(v_size)
V[:,0] = v_1
V[:,1] = v_2
V[:,2] = v_3

print(V)

VT = V.transpose()

print(VT)

a = U @ Sigma @ VT
print("check")
print(a)


print("----------------------------------")
# SVD
U, s, VT = svd(A)
print(U)
print(s)
print(VT)