import numpy as np

def solve_slae_kramer(matrix, vector):
    """
    Решает СЛАУ методом Крамера
    :param matrix: матрица коэффициентов (n x n)
    :param vector: вектор правых частей (n)
    :return: вектор решений (n)
    """
    n = len(matrix)
    if n != len(vector):
        raise ValueError("Размеры матрицы и вектора не совпадают")
    
    # Проверяем, квадратная ли матрица
    for row in matrix:
        if len(row) != n:
            raise ValueError("Матрица должна быть квадратной")
    
    det_A = np.linalg.det(matrix)
    if abs(det_A) < 1e-10:  # Практически нулевой определитель
        raise ValueError("Система не имеет единственного решения (det = 0)")
    
    solutions = []
    for i in range(n):
        # Создаем копию матрицы
        modified_matrix = [row.copy() for row in matrix]
        # Заменяем i-й столбец на вектор правых частей
        for j in range(n):
            modified_matrix[j][i] = vector[j]
        det_Ai = np.linalg.det(modified_matrix)
        solutions.append(det_Ai / det_A)
    
    return solutions

def input_matrix(n):
    """Ввод матрицы n x n с комплексными коэффициентами"""
    print(f"Введите матрицу {n}x{n} (по строкам, комплексные числа в формате a+bj):")
    matrix = []
    for i in range(n):
        while True:
            row_str = input(f"Строка {i+1}: ").split()
            if len(row_str) != n:
                print(f"Ожидается {n} элементов в строке")
                continue
            try:
                row = [complex(item) for item in row_str]
                matrix.append(row)
                break
            except ValueError:
                print("Некорректный формат числа. Используйте формат a+bj")
    return matrix

def input_vector(n):
    """Ввод вектора длины n с комплексными коэффициентами"""
    print(f"Введите вектор правых частей длины {n}:")
    while True:
        vector_str = input().split()
        if len(vector_str) != n:
            print(f"Ожидается {n} элементов в векторе")
            continue
        try:
            vector = [complex(item) for item in vector_str]
            return vector
        except ValueError:
            print("Некорректный формат числа. Используйте формат a+bj")

def main():
    print("Калькулятор СЛАУ методом Крамера")
    print("Поддерживаются комплексные коэффициенты (формат a+bj)")
    
    while True:
        try:
            n = int(input("Введите размер системы (n): "))
            if n < 1:
                print("Размер должен быть положительным числом")
                continue
            break
        except ValueError:
            print("Введите целое число")
    
    matrix = input_matrix(n)
    vector = input_vector(n)
    
    try:
        solutions = solve_slae_kramer(matrix, vector)
        print("\nРешения системы:")
        for i, sol in enumerate(solutions, 1):
            print(f"x{i} = {sol}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()