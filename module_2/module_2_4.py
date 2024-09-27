numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if 2 > i:
        continue
    is_prime = True
    for j in range(numbers[1], i):
        if i % j == 0:
            not_primes.append(i)
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(primes)
print(not_primes)
