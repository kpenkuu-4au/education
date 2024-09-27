data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    mix = 0

    def recursive_sum(x):
        nonlocal mix

        if isinstance(x, (int, float)):
            mix += x
        elif isinstance(x, str):
            mix += len(x)
        elif isinstance(x, (list, tuple, set)):
            for z in x:
                recursive_sum(z)
        elif isinstance(x, dict):
            for key, value in x.items():
                recursive_sum(key)
                recursive_sum(value)

    for i in args:
        recursive_sum(i)

    return mix


print(calculate_structure_sum(data_structure))
