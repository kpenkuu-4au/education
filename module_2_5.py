def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        for j in range(m):
            matrix.append([value] * n)
        return matrix


result1 = get_matrix(3, 1, 'Urban')
result2 = get_matrix(2, 2, True)
result3 = get_matrix(3, 2, 77)
print(result1)
print(result2)
print(result3)
