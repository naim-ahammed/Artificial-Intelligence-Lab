# Tuple: Create a tuple of student records (name, age, grade) and sort by grade.

students = [
    ("Naim", 20, 75),
    ("Fahim", 22, 62),
    ("Korim", 21, 78),
    ("Rahin", 23, 68),
    ("Labib", 19, 65)
]

SS = sorted(students, key=lambda student: student[2])
print(SS)
