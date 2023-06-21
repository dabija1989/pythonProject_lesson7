"""
Given two dictionaries representing students' grades:

math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

Write a program that prints out a new dictionary containing the average grades for each student.
"""
# Solution
math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

average_grades = {}

for name in math_grades:
    average_grades[name] = (math_grades[name] + science_grades[name]) / 2

for name, average_grade in average_grades.items():
    print(f"{name}: {average_grade}")