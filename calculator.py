# Function for addition
# This is Test
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display the menu and take input
def show_menu():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main function to run the calculator
def calculator():
    while True:
        show_menu()
        try:
            # Take user input for the operation
            choice = int(input("Enter choice (1/2/3/4/5): "))

            # Check for exit condition
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            # Input numbers for calculation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the selected operation
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}\n")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
            elif choice == 4:
                print(f"{num1} / {num2} = {divide(num1, num2)}\n")
            else:
                print("Invalid input! Please select a valid option.\n")

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    calculator()
