from Student import *

a = int(input("Enter the number of students:"))
total_list = []
total_students = []
i=1
while i <= a:
    student = Student()
    student.getmarks()
    total_students.append(student.name)
    total_list.append(student.total)
    i = i + 1

overall_total = sum(total_list)
print("Overall Marks:",overall_total)
print("All Students:",total_students)

res = {total_students[i]: total_list[i] for i in range(len(total_students))}

print("Resultant dictionary is : " + str(res))

keymax = max(zip(res.values(),res.keys()))[1]
print("The top performer:",keymax)