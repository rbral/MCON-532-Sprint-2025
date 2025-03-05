students_data = {
    101: {'name': 'Alice', 'grades': [85, 90, 88], 'gpa': round(sum([85, 90, 88]) / len([85, 90, 88]) / 25, 2)},
    102: {'name': 'Bob', 'grades': [78, 82, 80], 'gpa': round(sum([78, 82, 80]) / len([78, 82, 80]) / 25, 2)},
    103: {'name': 'Charlie', 'grades': [91, 94, 89], 'gpa': round(sum([91, 94, 89]) / len([91, 94, 89]) / 25, 2)}
}

import unittest

class TestStudentData(unittest.TestCase):

    def test_number_of_students(self):
        self.assertEqual(len(students_data), 3)

    def test_student_attributes(self):
        for student_id, data in students_data.items():
            self.assertIn('name', data)
            self.assertIn('grades', data)
            self.assertIn('gpa', data)

    def test_grades_type(self):
        for data in students_data.values():
            for grade in data['grades']:
                self.assertTrue(isinstance(grade, int))

if __name__ == '__main__':
    unittest.main()