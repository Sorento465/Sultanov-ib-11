students = []
perfect = []
for i in range(int(input())):
    students.append(input())
for student in students:
    print(student)
    if '4' in student or '5' in student:
        perfect.append(student)
print()
for perf in perfect:
    print(perf)