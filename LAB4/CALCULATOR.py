# calculator.py
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
def mod(a, b):
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    return a % b
def power(a, b): return a ** b

def get_two_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def menu():
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Power")
    print("7. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            a, b = get_two_numbers()
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            a, b = get_two_numbers()
            print(f"Result: {sub(a, b)}")
        elif choice == "3":
            a, b = get_two_numbers()
            print(f"Result: {mul(a, b)}")
        elif choice == "4":
            a, b = get_two_numbers()
            try:
                print(f"Result: {div(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            a, b = get_two_numbers()
            try:
                print(f"Result: {mod(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "6":
            a, b = get_two_numbers()
            print(f"Result: {power(a, b)}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-7.")

if __name__ == "__main__":
    main()