students = {
    101: {'name': 'Alice', 'grades': [85, 90, 88], 'gpa': round(sum([85, 90, 88]) / len([85, 90, 88]) / 25, 2)},
    102: {'name': 'Bob', 'grades': [79, 85, 92], 'gpa': round(sum([79, 85, 92]) / len([79, 85, 92]) / 25, 2)},
    103: {'name': 'Charlie', 'grades': [91, 87, 84], 'gpa': round(sum([91, 87, 84]) / len([91, 87, 84]) / 25, 2)}
}

for student_id, student_data in students.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {student_data['name']}")
    print(f"Grades: {student_data['grades']}")
    print(f"GPA: {student_data['gpa']}")
    print()