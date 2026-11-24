import datetime
import time
import math
import random
import string
import uuid
import importlib


# ==========================================
# DATETIME AND TIME MODULE
# ==========================================

def datetime_menu():

    while True:

        print("\n==========================")
        print("Datetime and Time Operations:")
        print("==========================")

        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            current = datetime.datetime.now()

            print("\nCurrent Date and Time:",
                  current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":

            try:

                first = input("\nEnter the first date (YYYY-MM-DD): ")
                second = input("Enter the second date (YYYY-MM-DD): ")

                date1 = datetime.datetime.strptime(first, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(second, "%Y-%m-%d")

                difference = abs((date2 - date1).days)

                print("Difference:", difference, "days")

            except ValueError:

                print("Invalid date format!")

        elif choice == "3":

            try:

                value = input("\nEnter date (YYYY-MM-DD): ")

                date_value = datetime.datetime.strptime(
                    value, "%Y-%m-%d"
                )

                print("Formatted Date:",
                      date_value.strftime("%d-%B-%Y"))

            except ValueError:

                print("Invalid date format!")

        elif choice == "4":

            input("\nPress Enter to start stopwatch...")

            start = time.perf_counter()

            input("Stopwatch running. Press Enter to stop...")

            end = time.perf_counter()

            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif choice == "5":

            try:

                seconds = int(input("\nEnter countdown time in seconds: "))

                if seconds < 0:
                    print("Time cannot be negative!")
                    continue

                for i in range(seconds, 0, -1):

                    print(i)
                    time.sleep(1)

                print("Countdown Completed!")

            except ValueError:

                print("Enter a valid number!")

        elif choice == "6":

            break

        else:

            print("Invalid choice! Try again.")

        print("==========================")


# ==========================================
# MATHEMATICAL OPERATIONS
# ==========================================

def math_menu():

    while True:

        print("\nMathematical Operations:")

        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:

                number = int(input("\nEnter a number: "))

                if number < 0:
                    print("Enter a non-negative number!")
                else:
                    print("Factorial:", math.factorial(number))

            except ValueError:

                print("Invalid number!")

        elif choice == "2":

            try:

                p = float(input("\nEnter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))

                if p < 0 or r < 0 or t < 0:
                    print("Values cannot be negative!")
                else:

                    amount = p * (1 + r / 100) ** t

                    print("Compound Interest:", f"{amount:.2f}")

            except ValueError:

                print("Invalid input!")

        elif choice == "3":

            try:

                angle = float(input("\nEnter angle in degrees: "))

                radians = math.radians(angle)

                print("Sine:", round(math.sin(radians), 4))
                print("Cosine:", round(math.cos(radians), 4))
                print("Tangent:", round(math.tan(radians), 4))

                number = float(input("Enter a positive number for logarithm: "))

                if number > 0:
                    print("Logarithm:", round(math.log(number), 4))
                else:
                    print("Enter a positive number!")

            except ValueError:

                print("Invalid input!")

        elif choice == "4":

            print("\n1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape = input("Choose a shape: ")

            try:

                if shape == "1":

                    radius = float(input("Enter radius: "))

                    area = math.pi * radius ** 2

                    print("Area of Circle:", round(area, 2))

                elif shape == "2":

                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))

                    area = length * width

                    print("Area of Rectangle:", round(area, 2))

                elif shape == "3":

                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))

                    area = 0.5 * base * height

                    print("Area of Triangle:", round(area, 2))

                else:

                    print("Invalid shape!")

            except ValueError:

                print("Invalid dimensions!")

        elif choice == "5":

            break

        else:

            print("Invalid choice!")

        print("==========================")


# ==========================================
# RANDOM DATA GENERATION
# ==========================================

def random_menu():

    while True:

        print("\nRandom Data Generation:")

        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Simulate Random Sampling")
        print("6. Game Simulation")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                low = int(input("\nEnter minimum number: "))
                high = int(input("Enter maximum number: "))

                print("Random Number:", random.randint(low, high))

            elif choice == "2":

                size = int(input("\nEnter list size: "))
                low = int(input("Enter minimum value: "))
                high = int(input("Enter maximum value: "))

                if size < 0 or low > high:
                    print("Invalid input!")
                else:

                    numbers = [
                        random.randint(low, high)
                        for i in range(size)
                    ]

                    print("Random List:", numbers)

            elif choice == "3":

                length = int(input("\nEnter password length: "))

                if length < 1:
                    print("Length must be at least 1!")
                else:

                    characters = string.ascii_letters + string.digits + "!@#$%&*?"

                    password = ''.join(
                        random.choice(characters)
                        for i in range(length)
                    )

                    print("Generated Password:", password)

            elif choice == "4":

                length = int(input("\nEnter OTP length: "))

                if length < 1:
                    print("Length must be at least 1!")
                else:

                    otp = ''.join(
                        random.choice(string.digits)
                        for i in range(length)
                    )

                    print("Generated OTP:", otp)

            elif choice == "5":

                data = input("\nEnter items separated by commas: ").split(",")

                size = int(input("Enter sample size: "))

                if 0 <= size <= len(data):

                    print("Random Sample:", random.sample(data, size))

                else:

                    print("Invalid sample size!")

            elif choice == "6":

                user = random.randint(1, 6)
                computer = random.randint(1, 6)

                print("\nYour Dice:", user)
                print("Computer Dice:", computer)

                if user > computer:
                    print("You Win!")
                elif user < computer:
                    print("Computer Wins!")
                else:
                    print("It's a Draw!")

            elif choice == "7":

                break

            else:

                print("Invalid choice!")

        except ValueError:

            print("Please enter valid values!")

        print("==========================")


# ==========================================
# UUID MODULE
# ==========================================

def uuid_menu():

    print("\nGenerate Unique Identifiers (UUID):")

    unique_id = uuid.uuid4()

    print("Generated UUID:", unique_id)

    print("==========================")


# ==========================================
# FILE OPERATIONS
# ==========================================

def file_menu():

    while True:

        print("\nFile Operations:")

        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                filename = input("\nEnter file name: ")

                with open(filename, "w") as file:
                    pass

                print("File created successfully!")

            elif choice == "2":

                filename = input("\nEnter file name: ")

                data = input("Enter data to write: ")

                with open(filename, "w") as file:

                    file.write(data)

                print("Data written successfully!")

            elif choice == "3":

                filename = input("\nEnter file name: ")

                with open(filename, "r") as file:

                    content = file.read()

                print("File Content:")
                print(content)

            elif choice == "4":

                filename = input("\nEnter file name: ")

                data = input("Enter data to append: ")

                with open(filename, "a") as file:

                    file.write("\n" + data)

                print("Data appended successfully!")

            elif choice == "5":

                break

            else:

                print("Invalid choice!")

        except FileNotFoundError:

            print("File not found!")

        except OSError as e:

            print("File Error:", e)

        print("==========================")


# ==========================================
# DYNAMIC MODULE EXPLORATION
# ==========================================

def explore_module():

    print("\nExplore Module Attributes:")

    name = input("Enter module name to explore: ")

    try:

        module = importlib.import_module(name)

        print(f"\nAvailable Attributes in {name} module:")

        print(dir(module))

    except ImportError:

        print("Module not found!")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n==========================")
        print("Welcome to Multi-Utility Toolkit")
        print("==========================")

        print("Choose an option:")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":

            datetime_menu()

        elif choice == "2":

            math_menu()

        elif choice == "3":

            random_menu()

        elif choice == "4":

            uuid_menu()

        elif choice == "5":

            file_menu()

        elif choice == "6":

            explore_module()

        elif choice == "7":

            print("\n==========================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("==========================")

            break

        else:

            print("Invalid choice! Please select 1 to 7.")


# ==========================================
# MAIN PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":

    main()
