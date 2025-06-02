def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def assign_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def print_student_report(student):
    name = student["name"]
    grades = student["grades"]
    average = calculate_average(grades)
    letter = assign_letter_grade(average)
    print(f"Report for {name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter}")
    print("-" * 30)

def process_all_students(students):
    for student in students:
        print_student_report(student)

def main():
    students = [
        {"name": "Alice", "grades": [88, 92, 79]},
        {"name": "Bob", "grades": [75, 70, 68]},
        {"name": "Charlie", "grades": [95, 100, 98]},
        {"name": "Daisy", "grades": [58, 62, 55]},
    ]
    process_all_students(students)

if __name__ == "__main__":
    main()
