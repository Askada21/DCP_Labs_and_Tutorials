from pathlib import Path

import pandas as pd

LAB_DIR = Path(__file__).resolve().parent
MARKS = ["engagement", "assignment", "exam"]

def load_students():
    # Step 1: read the csv into a pandas DataFrame
    df = pd.read_csv(LAB_DIR / "data" / "exams.csv")
    # Bonus: record which rows have missing marks before filling them
    incomplete = df[MARKS].isna().any(axis=1)
    # Step 2: use zero for missing marks and store all marks as integers
    df[MARKS] = df[MARKS].fillna(0).astype(int)

    # Step 4: calculate weighted totals for all students and round to one decimal
    df["total"] = (
        df["engagement"] * 0.2
        + df["assignment"] * 0.3
        + df["exam"] * 0.5
    ).round(1)
    # A pass requires at least 40 in both the total and the exam
    passed = df["total"].ge(40) & df["exam"].ge(40)
    df["result"] = passed.map({True: "Pass", False: "Fail"})

    # Check the new columns in the first five rows
    print(df.head())
    # Bonus: sort by last name for display and export
    return df.sort_values("last", kind="stable"), incomplete


def print_csv(students):
    # Print csv rows without a header or DataFrame index
    print(students.to_csv(index=False, header=False, float_format="%.1f"), end="")


def find_student(df):
    # Step 3: look up the student number, then print the marks, total, and result
    number = input("Enter student number: ").strip().upper()
    matches = df.loc[df["number"].eq(number)]

    if matches.empty:
        print("Not found")
        return

    student = matches.iloc[0]
    print(f"Name: {student['last']}, {student['first']}")
    print(f"Number: {student['number']}")
    print(f"Engagement: {student['engagement']}")
    print(f"Assignment: {student['assignment']}")
    print(f"Exam: {student['exam']}")
    print(f"Total: {student['total']:.1f}")
    print(f"Result: {student['result']}")


def login():
    # Bonus: give the user three login attempts before showing the menu
    for attempts_left in range(2, -1, -1):
        username = input("Username: ")
        password = input("Password: ")
        if username == "admin" and password == "python123":
            return True

        print(f"Incorrect login. Attempts left: {attempts_left}")

    print("Too many failed attempts.")
    return False


def menu(df, incomplete):
    # Step 5: keep showing the menu until the user chooses Quit
    while True:
        print("\nStudent Management System")
        print("1. All marks")
        print("2. Pass")
        print("3. Fail")
        print("4. Find student")
        print("5. Quit")
        print("6. Incomplete records")
        print("7. Save results to CSV")

        choice = input("Choice: ").strip()
        if choice == "1":
            print_csv(df)
        elif choice == "2":
            # Select passing students and count the selected rows
            passed = df.loc[df["result"].eq("Pass")]
            print_csv(passed)
            print(f"Total passed: {len(passed)}")
        elif choice == "3":
            # Select failing students and count the selected rows
            failed = df.loc[df["result"].eq("Fail")]
            print_csv(failed)
            print(f"Total failed: {len(failed)}")
        elif choice == "4":
            find_student(df)
        elif choice == "5":
            print("Goodbye!")
            break
        elif choice == "6":
            # Use the saved mask to find rows that originally had missing marks
            incomplete_students = df.loc[incomplete]
            print_csv(incomplete_students)
            print(f"Total incomplete records: {len(incomplete_students)}")
        elif choice == "7":
            # Bonus: export all student records with column headings
            df.to_csv(LAB_DIR / "results.csv", index=False, float_format="%.1f")
            print("Results saved to results.csv")
        else:
            print("Invalid choice. Try again.")


def main():
    if login():
        df, incomplete = load_students()
        menu(df, incomplete)


if __name__ == "__main__":
    main()
