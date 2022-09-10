from numpy import delete, s_


def main():
    m = int(input("Количество строк умножаемой матрицы: "))
    w = int(input("Количество столбцов умножаемой матрицы: "))
    n = int(input("Количество строк матрицы- множителя: "))
    k = int(input("Количество столбцов матрицы-множителя: "))

    if w != n:
        print("Матрицы невозможно перемножить!")
        exit(404)

    a = []
    b = []
    for i in range(0, w):
        print("Введите " + str(i + 1) + " строку умножаемой матрицы")
        massOfStrings = list(map(int, input().split(' ')))
        if len(massOfStrings) != m:
            print("Количество элементов строки больше, чем ожидалось!")
            exit(404)
        a.append(massOfStrings)

    for i in range(0, k):
        print("Введите " + str(i + 1) + " строку матицы-множителя")
        massOfStrings = list(map(int, input().split(' ')))
        if len(massOfStrings) != n:
            print("Количество элементов строки больше или меньше, чем ожидалось!")
            exit(404)
        b.append(massOfStrings)

    c = [[None for __ in range(k)] for __ in range(m)]

    for i in range(m):
        for j in range(k):
            c[i][j] = sum(a[i][q] * b[q][j] for q in range(n))

    print("Результирующая матрица: ")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in c]))

    if len(c) != len(c[0]) or len(c) == 1:
        print("Невозможно найти определитель матрицы, так как матрица не является квадратной!")
    else:
        print("Определитель полученной матрицы: ")
        print(find_det(c))


def find_det(matrix):
    if len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    if len(matrix) == 3:
        det = 0
        length = len(matrix[0])
        for j in range(length):
            m = delete(matrix, [0], 0)
            m = delete(m, s_[j], 1)
            det += (-1)**(1 + j + 1) * matrix[0][j] * find_det(m)
        return det


if __name__ == '__main__':
    main()
