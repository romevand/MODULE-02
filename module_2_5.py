# Функции в Python.Функция с параметром.

# Задача "Матрица во плоти"

# Программа представляет собой функцию get_matrix с тремя входными параметрами: n, m и value,
# которая создаёт матрицу (вложенный список) размером в n строк и m столбцов, заполненную значениями value,
# и возвращает эту матрицу в качестве результата работы.

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

print("\nПолучить матрицу размером 2 х 2, заполненную значением 10:")
result1 = get_matrix(2, 2, 10)
print(result1)

print("\nПолучить матрицу размером 3 х 5, заполненную значением 42:")
result2 = get_matrix(3, 5, 42)
print(result2)

print("\nПолучить матрицу размером 4 х 2, заполненную значением 13:")
result3 = get_matrix(4, 2, 13)
print(result3)

print('\nРабота завершена.')