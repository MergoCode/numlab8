import numpy as np

def read_n(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

def norma_vector_diff(Y, X):
    return np.max(np.abs(Y - X))

def norma_matrix(X):
    return np.max(np.sum(np.abs(X), axis=1))

def method_gauss_seidel(A, B, X0, X1, n, k):
    kmax = 100000
    eps = 1e-14
    print("\nMethod Gauss-Seidel\n")
    k[0] = 1

    while True:
        # Копіюємо попереднє значення X1 до X0
        np.copyto(X0, X1)

        for i in range(n):
            sum_ = 0.0
            for j in range(n):
                if j < i:
                    sum_ += A[i][j] * X1[j]
                elif j > i:
                    sum_ += A[i][j] * X0[j]

            X1[i] = (B[i] - sum_) / A[i][i]

        k[0] += 1
        if k[0] > kmax:
            print("Solution not found!")
            break
        
        if norma_vector_diff(X1, X0) < eps:
            print("Solution found!")
            print(f"Iteration: {k[0]}")
            break

def method_jacobi(A, B, X0, X1, n, k):
    kmax = 100000
    eps = 1e-14
    print("\nMethod Jacobi\n")
    k[0] = 1
    
    while True:
        np.copyto(X0, X1)

        for i in range(n):
            sum_ = sum(A[i][j] * X0[j] for j in range(n) if j != i)
            X1[i] = (B[i] - sum_) / A[i][i]

        k[0] += 1
        if k[0] > kmax:
            print("Solution not found!")
            break
        
        if norma_vector_diff(X1, X0) < eps:
            print("Solution found!")
            print(f"Iteration: {k[0]}")
            break

def method_simple_iteration(A, B, X0, X1, n, k, tau):
    kmax = 100000
    eps = 1e-14
    print("\nSimple Iteration\n")
    k[0] = 1

    while True:
        np.copyto(X0, X1)

        for i in range(n):
            sum_ = np.dot(X0, A[i])
            X1[i] = X0[i] - tau * sum_ + tau * B[i]

        k[0] += 1
        if k[0] > kmax:
            print("Solution not found!")
            break
        
        if norma_vector_diff(X1, X0) < eps:
            print("Solution found!")
            print(f"Iteration: {k[0]}")
            break

def main():
    matrix_A_filename = "matrix_A.txt"
    matrix_B_filename = "matrix_B.txt"
    matrix_XI_filename = "matrix_XI.txt"
    matrix_XG_filename = "matrix_XG.txt"
    matrix_XY_filename = "matrix_XY.txt"
    output_filename = "output.txt"
    
    n = read_n(matrix_A_filename)
    print(n)

    B = np.zeros(n)
    X0 = np.zeros(n)
    X1 = np.zeros(n)
    A = np.zeros((n, n))

    with open(matrix_A_filename, 'r') as f:
        for i in range(n):
            A[i] = np.array(list(map(float, f.readline().split())), dtype=np.float64)

    for i in range(n):
        B[i] = np.sum(A[i]) * 2.51  # x = 2.51 as per original code

    with open(matrix_B_filename, 'w') as f:
        for value in B:
            f.write(f"{value:.10e}\n")

    tau = 1 / norma_matrix(A)
    k = [1]

    method_simple_iteration(A, B, X0, X1, n, k, tau)

    with open(matrix_XI_filename, 'w') as f:
        for value in X1:
            f.write(f"{value:.10e}\n")
    
    with open(output_filename, 'a') as f:
        f.write(f"SI\t{str(k[0])}\n")

    k[0] = 1
    X1.fill(0.0)
    method_jacobi(A, B, X0, X1, n, k)

    with open(matrix_XY_filename, 'w') as f:
        for value in X1:
            f.write(f"{value:.10e}\n")

    with open(output_filename, 'a') as f:
        f.write(f"Ya\t{str(k[0])}\n")

    k[0] = 1
    X1.fill(0.0)
    method_gauss_seidel(A, B, X0, X1, n, k)

    with open(matrix_XG_filename, 'w') as f:
        for value in X1:
            f.write(f"{value:.10e}\n")

    with open(output_filename, 'a') as f:
        f.write(f"GZ\t{str(k[0])}\n")

if __name__ == "__main__":
    main()
