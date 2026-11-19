# Employee Salary Management System

FILE_NAME = "employees.txt"


def add_employee(name, emp_id, salary):
    """Takes name, ID and salary and appends one record to the file."""
    # "a" mode: existing data thakbe, notun line add hobe
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{name} | {emp_id} | {salary}\n")
    return True  # Success hole True return korbe


def view_employees():
    """Reads employees.txt and displays all records."""
    try:
        # "r" mode: shudhu read korbe
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No employee records found.")
        return []

    if not lines:
        print("No employee records found.")
        return []

    print("\nEmployee Records:")
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip()}")
    return lines


def main():
    """Main menu loop."""
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Choose Option: ").strip()

        if choice == "1":
            name = input("Enter Name: ").strip()
            emp_id = input("Enter ID: ").strip()
            salary = input("Enter Salary: ").strip()

            # Salary number kina check korchi
            if not salary.isdigit():
                print("Salary must be a number. Try again.")
                continue

            if add_employee(name, emp_id, salary):
                print("Employee Added Successfully")

        elif choice == "2":
            view_employees()

        elif choice == "3":
            print("Exiting program. Bye!")
            break

        else:
            print("Invalid option. Please choose 1, 2 or 3.")


# Program shuru hobe ekhan theke
if __name__ == "__main__":
    main()
