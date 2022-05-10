import numpy as np
A = (np.random.random((np.random.randint(1, 100), np.random.randint(1, 100))))

ATA = np.matmul(A, A.T)
AAT = np.matmul(A.T, A)

print('A^T * A symmetric :', np.all(ATA==ATA.T))
print('A * A^T symmetric :', np.all(AAT==AAT.T))

try:
    U, S, Vh = np.linalg.svd(A)
    print(f'SVD : U={U.shape}, S={S.shape}, V^h={Vh.shape}')
    eigval, eigvec = np.linalg.eig(A)
    print(f'EIG : eigval={eigval.shape}, eigvec={eigvec.shape}')
except Exception as e:
    print('[Eigen Decomposition Error]', e)
finally:
    print(f'A={A.shape}')