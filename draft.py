
def task_7(students):

    array_students = []

    for i in range(students):
        math_grade = rand(0, 50)
        programming_grade = rand(0, 50)
        sum_points = math_grade + programming_grade
        array_students.append((math_grade, programming_grade, sum_points))
    max_student = max(array_students, key=lambda x: x[2])
    max_points = max_student[2]
    max_students = [student for student in array_students if student[2] == max_points]
    print(f"Студенты:", array_students)
    print(f"Максимальное значение по sum_points:", max_points, max_student)
    for student in max_students:
        print(
            f"Math Grade: {student[0]}, Programming Grade: {student[1]}, Sum Points: {student[2]}"
        )
    return array_students


task_7(int(input("Enter how many students wrote test: ")))