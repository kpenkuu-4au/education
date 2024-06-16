students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
stud = sorted(list(students))
grad = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
st_gr = [[stud[0], grad[0]], [stud[1], grad[1]], [stud[2], grad[2]], [stud[3], grad[3]], [stud[4], grad[4]]]
dictstgr = dict(st_gr)
print(dictstgr)


