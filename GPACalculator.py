# GPA Calculator - By Youssef Khaled
print("=== GPA Calculator ===")
grades = []
for i in range(3):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

gpa = sum(grades) / len(grades)
print("Your GPA is:", round(gpa, 2))