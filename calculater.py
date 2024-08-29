def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def get_user_choice():
    """Get the user's choice of operation"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")
    return choice

def get_numbers():
    """Get two numbers from the user"""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def main():
    while True:
        choice = get_user_choice()

        # Check if choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(e)

        else:
            print("Invalid input")

        # Ask if user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()