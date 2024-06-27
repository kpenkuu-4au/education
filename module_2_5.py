def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        string = []
        matrix.append(string)
        for j in range(m):
            string.append(value)
    return matrix


result1 = get_matrix(3, 1, 'Urban')
result2 = get_matrix(2, 2, True)
result3 = get_matrix(4, 2, 11)
print(result1)
print(result2)
print(result3)
