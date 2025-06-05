def main():
    students = [
        {"name": "Alice", "grades": [88, 92, 79]},
        {"name": "Bob", "grades": [75, 70, 68]},
        {"name": "Charlie", "grades": [95, 100, 98]},
        {"name": "Daisy", "grades": [58, 62, 55]},
    ]

    for student in students:
        name = student["name"]
        grades = student["grades"]
        
        if not grades:
            average = 0
        else:
            average = sum(grades) / len(grades)
        
        if average >= 90:
            letter = 'A'
        elif average >= 80:
            letter = 'B'
        elif average >= 70:
            letter = 'C'
        elif average >= 60:
            letter = 'D'
        else:
            letter = 'F'
        
        print(f"Report for {name}")
        print(f"Grades: {grades}")
        print(f"Average: {average:.2f}")
        print(f"Letter Grade: {letter}")
        print("-" * 30)

if __name__ == "__main__":
    main()
