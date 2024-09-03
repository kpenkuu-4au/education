from itertools import combinations


def all_variants(text):
    for index in range(len(text)):
        for letters in combinations(text, index + 1):
            yield ''.join(letters)


a = all_variants("abc")

for i in a:
    print(i)
