"""
Student Grade Calculator

A beginner-friendly Python program that asks for a student's marks,
calculates the average, and displays a grade.

Note: This is a simple example implementation. Adjust the grading
thresholds to match your course or institution's rules.
"""


def calculate_grade(average):
    """Return a letter grade based on the average mark."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    print("Student Grade Calculator")

    try:
        count = int(input("How many subjects? "))
        if count <= 0:
            print("Please enter a number greater than zero.")
            return

        marks = []
        for subject in range(1, count + 1):
            mark = float(input(f"Enter mark for subject {subject} (0-100): "))
            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(mark)

        average = sum(marks) / len(marks)
        grade = calculate_grade(average)

        print(f"Average mark: {average:.2f}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter numbers where requested.")


if __name__ == "__main__":
    main()
