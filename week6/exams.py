# Student Management System
students = {}

# Step 1 - print the original file
def print_file():
    with open("exams.prn") as f:
        for line in f:
            print(line, end="")


# Step 2 and 3 - extract fields and store records
def load_students():
    with open("exams.prn") as f:
        header = f.readline()  # skip the header

        for line in f:
            if not line.strip():
                continue

            last = line[0:14].strip()
            first = line[14:25].strip()
            number = line[25:42].strip()

            engagement_text = line[42:56].strip()
            assignment_text = line[56:68].strip()
            exam_text = line[68:80].strip()

            # convert missing marks to 0
            engagement = int(engagement_text) if engagement_text else 0
            assignment = int(assignment_text) if assignment_text else 0
            exam = int(exam_text) if exam_text else 0

            student = {
                "last": last,
                "first": first,
                "number": number,
                "engagement": engagement,
                "assignment": assignment,
                "exam": exam,
                "incomplete": (
                    engagement_text == ""
                    or assignment_text == ""
                    or exam_text == ""
                )
            }

            students[number] = student


# Step 4 - calculate total mark
def calculate_total(student):
    total = (
        student["engagement"] * 0.2
        + student["assignment"] * 0.3
        + student["exam"] * 0.5
    )
    return total


# Step 4 - pass or fail
def result(student):
    total = calculate_total(student)

    if total >= 40 and student["exam"] >= 40:
        return "Pass"
    else:
        return "Fail"


# print a student in csv format
def print_csv(student):
    total = calculate_total(student)

    print(
        f'{student["last"]},'
        f'{student["first"]},'
        f'{student["number"]},'
        f'{student["engagement"]},'
        f'{student["assignment"]},'
        f'{student["exam"]},'
        f'{total:.1f},'
        f'{result(student)}'
    )


# print a student's detailed record
def print_student(student):
    print(f'Name: {student["last"]}, {student["first"]}')
    print(f'Number: {student["number"]}')
    print(f'Engagement: {student["engagement"]}')
    print(f'Assignment: {student["assignment"]}')
    print(f'Exam: {student["exam"]}')
    print(f'Total: {calculate_total(student):.1f}')
    print(f'Result: {result(student)}')
    print()


# bonus - sort students alphabetically by last name
def sorted_students():
    return sorted(
        students.values(),
        key=lambda student: student["last"]
    )


# Step 5 - option 1: all marks
def all_marks():
    for student in sorted_students():
        print_csv(student)


# Step 5 - option 2: passed students
def passed_students():
    count = 0

    for student in sorted_students():
        if result(student) == "Pass":
            print_csv(student)
            count += 1

    print(f"\nTotal passed: {count}")


# Step 5 - option 3: failed students
def failed_students():
    count = 0

    for student in sorted_students():
        if result(student) == "Fail":
            print_csv(student)
            count += 1

    print(f"\nTotal failed: {count}")


# Step 5 - option 4: find student
def find_student():
    number = input("Enter student number: ").strip()

    if number in students:
        print_student(students[number])
    else:
        print("Not found")


# bonus - show incomplete records
def incomplete_students():
    count = 0

    for student in sorted_students():
        if student["incomplete"]:
            print_csv(student)
            count += 1

    print(f"\nTotal incomplete records: {count}")


# bonus - save results to csv file
def save_results():
    with open("results.csv", "w") as f:
        f.write(
            "Last,First,Number,Engagement,"
            "Assignment,Exam,Total,Result\n"
        )

        for student in sorted_students():
            total = calculate_total(student)

            line = (
                f'{student["last"]},'
                f'{student["first"]},'
                f'{student["number"]},'
                f'{student["engagement"]},'
                f'{student["assignment"]},'
                f'{student["exam"]},'
                f'{total:.1f},'
                f'{result(student)}\n'
            )

            f.write(line)

    print("Results saved to results.csv")


# bonus - username and password (3 attempts)
def login():
    username = "admin"
    password = "python123"

    for attempt in range(3):
        entered_username = input("Username: ")
        entered_password = input("Password: ")

        if entered_username == username and entered_password == password:
            print("Login successful!\n")
            return True
        else:
            print(f"Incorrect login. Attempts left: {2 - attempt}")

    print("Too many failed attempts.")
    return False


# Step 5 - Menu
def menu():
    while True:
        print("\nStudent Management System")
        print("1. All marks")
        print("2. Pass")
        print("3. Fail")
        print("4. Find student")
        print("5. Quit")
        print("6. Incomplete records (Bonus)")
        print("7. Save results to CSV (Bonus)")

        choice = input("Choice: ")

        if choice == "1":
            all_marks()

        elif choice == "2":
            passed_students()

        elif choice == "3":
            failed_students()

        elif choice == "4":
            find_student()

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            incomplete_students()

        elif choice == "7":
            save_results()

        else:
            print("Invalid choice. Try again.")


# MAIN PROGRAM
def main():
    print("STEP 1 - Original file:\n")
    print_file()

    print("\n\nSTEP 2 & 3 - Loading students:\n")
    load_students()

    # print extracted fields for each student (step 2)
    for student in students.values():
        print(f'Name: {student["last"]}, {student["first"]}')
        print(f'Number: {student["number"]}')
        print(f'Engagement: {student["engagement"]}')
        print(f'Assignment: {student["assignment"]}')
        print(f'Exam: {student["exam"]}')
        print()

    print(f"Total students loaded: {len(students)}")

    if login():
        menu()


if __name__ == "__main__":
    main()
