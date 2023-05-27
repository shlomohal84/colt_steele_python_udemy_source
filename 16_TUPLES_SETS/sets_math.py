

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

all_students = math_students | biology_students  # union

print(all_students)

duplicated_students = math_students & biology_students  # intersection
print(duplicated_students)
