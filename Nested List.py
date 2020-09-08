# nested list
physics_students = []
n = int(input())
for x in range(n):
    name = input()
    score = float(input())
    student = [name, score]
    physics_students.append(student)
N = len(physics_students)

grade_list = []
for i in range(N):
    grade_list.append(physics_students[i][1])
grade_list.sort()
min_grade = min(grade_list)
grade_list_temp = grade_list[:]
for i in range(len(grade_list)):
    if grade_list[i] == min_grade:
        grade_list_temp.pop(0)
    else:
        pass
low2nd_name_list = []
for i in range(N):
    if physics_students[i][1] == grade_list_temp[0]:
        low2nd_name_list.append(physics_students[i][0])
for name in low2nd_name_list:
    print(name)


















