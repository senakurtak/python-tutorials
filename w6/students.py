
#listede [isim, yaş, not]

school = []
school.append(["Sena", 27, 80.9])
school.append(["Sude", 24, 60.9])
school.append(["Buse", 26, 40.2])
school.append(["Asu", 28, 70.3])
school.append(["Canan", 25, 84.2])

print(school)

'''for student in school:
    print(student[0])'''

'''for i in range(len(school)):
    print(school[i][0])
'''

# Örnekler
def bestStudent(values):
    max_grade = 0
    best_student = ""
    for student in values:
        if student[2] > max_grade:
            max_grade = student[2]
            best_student = student[0]
    return best_student

print("best student is", bestStudent(school))

def allPass(values, criteria): # kriterlere göre öğrencinin geçip geçmeyeceğini söylüyor
    for i in values:
        if i[2] > criteria:
            print(i[0], "will pass the course!")

allPass(school, 50)
