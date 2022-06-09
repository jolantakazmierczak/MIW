import numpy as np
from numpy.linalg import eig
from scipy.linalg import svd
# A = U . Sigma . V^T


def svd(A):
    # transpozycja macierzy A
    AT = A.transpose()
    AAT = A @ AT  # A*A^T

    # U
    eigenValues_AAT, eigenVectors_AAT = eig(AAT)  # wartości i wektory własne dla A*A^T
    idx = eigenValues_AAT.argsort()[::-1]  # sortowanie po wartościach własnych od największej do najmniejszej
    lambdas_u = eigenValues_AAT[idx] # ułożenie lambd od największej do najmniejszej
    U = eigenVectors_AAT[:, idx]   # macierz U // sortowanie wektorów własnych rosnąco według lambd

    # Sigma
    sigmas = np.sqrt(lambdas_u)   # wyliczenie sigm poprzez boliczenie pierwiastków z lambd


    size = (len(A), len(A[0])) # obliczenie rozmiaru dla Sigma

    Sigma = np.zeros(size) # Stworzenie macierzy z zerami o wyliczonym rozmiarze
    np.fill_diagonal(Sigma, Sigma.diagonal() + sigmas) # dodanie na przekątnej sigm

    # V1
    # u1 i u2
    u_1 = U[:, 0]
    u_2 = U[:, 1]

    # sigma_1 i sigma_2
    sigma_1 = np.reciprocal(sigmas[0])
    sigma_2 = np.reciprocal(sigmas[1])

    # v1 i v2
    v_1 = AT @ u_1 * sigma_1
    v_2 = AT @ u_2 * sigma_2

    # v3

    ATA = AT @ A

    eigenvalues_ATA, eigenvectors_ATA = np.linalg.eig(ATA)
    ATA_sorted = np.flip(np.argsort(eigenvalues_ATA))
    eigenvectors_ATA = eigenvectors_ATA[:, ATA_sorted]

    v_3 = eigenvectors_ATA[:, 2]

    v_size = (len(A[0]), len(A[0]))
    V = np.zeros(v_size)
    V[:, 0] = v_1
    V[:, 1] = v_2
    V[:, 2] = v_3

    VT = V.transpose()

    return U, Sigma, VT

A = np.array([
    [1,2,0],
    [2,0,2],

])


U, Sigma, VT = svd(A)

print("A = ")
print(A)
print("---------")
print("U = ")
print(U)
print("---------")
print("Sigma = ")
print(Sigma)
print("---------")
print("VT = ")
print(VT)
print("---------------------------------")


a = U @ Sigma @ VT
print("A = U*Sigma*VT = ")
print(a)