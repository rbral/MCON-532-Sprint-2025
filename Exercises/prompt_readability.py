# Create student dictionary using dictionary comprehension
students = {
    id: {'name': name, 'grades': grades, 'gpa': round(sum(grades) / len(grades) / 25, 2)}
    for id, (name, grades) in {
        101: ('Alice', [85, 90, 88, 92]),
        102: ('Bob', [75, 80, 78, 82]),
        103: ('Charlie', [90, 92, 85, 88])
    }.items()
}

# Print student data in a well-structured format
for id, data in students.items():
    print(f'Student ID: {id}')
    print(f'Name: {data["name"]}')
    print(f'Grades: {data["grades"]}')
    print(f'GPA: {data["gpa"]}')
    print()