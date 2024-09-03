def is_prime(fun):
    def wrapper(*args):
        orig_result = fun(*args)

        def prime(number):
            if number % 2 == 0:
                return number == 2
            x = 3
            while x * x <= number and number % x != 0:
                x += 2
            return x * x > number

        if prime(orig_result) is False:
            print('Составное')
        else:
            print('Простое')
        return orig_result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result1 = sum_three(2, 3, 6)
print(result1)
result2 = sum_three(3, 4, 5)
print(result2)
