x = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result = []


def keys(n=int(input())):
    for i in x:
        for j in range(3, 20):
            if n % (j + i - 1) == 0 and i == 1:
                result.append(str(i) + str(j - 1))
    for i in range(1, 20):
        for j in x:
            if i == j:
                break
            elif n == i + j and j != n - 1:
                result.append(str(i) + str(j))
                j += 1
    return result


keys()
print(''.join(result))
