def transpose_matrix(matrix):

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:3}", end=" ")
        print()

def main():

    print("Введите матрицу в формате: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")

    matrix_input = input("\nВведите матрицу: ")
    matrix = eval(matrix_input)

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        print("Ошибка: введена не матрица!")
        return

    print("Исходная матрица:")
    print(print_matrix(matrix))

    transposed = transpose_matrix(matrix)

    print("Транспонированная матрица:")
    print(print_matrix(transposed))

if __name__ == "__main__":
    main()