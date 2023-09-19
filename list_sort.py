
"""
num_list = [1,3,5,2,4]
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)


str = ['Jack','Lin','Tom','Andy','z']
print(str)
str.sort()
print(str)
str.sort(reverse=True)
print(str)
"""


# Tuple
students = [
  ("小明",170,"C"),
  ("小华",150,"B"),
  ("小明",160,"A")
]

sorted_students = sorted(students,key=lambda student:student[1])
print(sorted_students)

