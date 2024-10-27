import random

n = 100
scale = 10
a, b = 1, 9
A = [[0] * (n + 1) for _ in range(n + 1)]

# Встановлюємо насіння для випадкових чисел
random.seed()

with open("matrix_A.txt", "w") as matrix_A:
    for i in range(1, n + 1):
        sum_elements = 0
        for j in range(1, n + 1):
            A[i][j] = a + b * random.random()
            if i != j:
                sum_elements += A[i][j]
        
        # Діагональний елемент задаємо так, щоб матриця була діагонально домінантною
        A[i][i] = sum_elements * scale

    # Записуємо матрицю у файл
    for i in range(1, n + 1):
        for j in range(1, n):
            matrix_A.write(f"{A[i][j]:.6e}\t")
        matrix_A.write(f"{A[i][n]:.6e}\n")
