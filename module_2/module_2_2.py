first = 111
second = 1
third = 11
if first == second == third:
    print(3)
elif not first == second == third:
    print(0)
elif first == second != third or first != second == third or first == third != second:
    print(2)