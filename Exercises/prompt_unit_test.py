# Creating a Python dictionary using dictionary comprehension
students_dict = {
    101: {'name': 'Alice', 'grades': [85, 79, 91], 'gpa': round(sum([85, 79, 91]) / len([85, 79, 91]) / 25, 2)},
    102: {'name': 'Bob', 'grades': [92, 88, 75], 'gpa': round(sum([92, 88, 75]) / len([92, 88, 75]) / 25, 2)},
    103: {'name': 'Charlie', 'grades': [80, 86, 90], 'gpa': round(sum([80, 86, 90]) / len([80, 86, 90]) / 25, 2)}
}

# Unit tests using unittest
import unittest

class TestStudentData(unittest.TestCase):

    def test_number_of_students(self):
        self.assertEqual(len(students_dict), 3)

    def test_student_details(self):
        for student_id, student_data in students_dict.items():
            self.assertIn('name', student_data)
            self.assertIn('grades', student_data)
            self.assertIn('gpa', student_data)

    def test_grades_are_integers(self):
        for student_id, student_data in students_dict.items():
            grades = student_data['grades']
            self.assertTrue(all(isinstance(grade, int) for grade in grades))

if __name__ == '__main__':
    unittest.main()