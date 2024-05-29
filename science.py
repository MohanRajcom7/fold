import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("1. Square Root")
    print("2. Power")
    print("3. Trigonometric Functions")
    print("4. Logarithm")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            num = float(input("Enter a number: "))
            print("Square root:", math.sqrt(num))
        elif choice == '2':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print("Result:", math.pow(base, exponent))
        elif choice == '3':
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            trig_choice = input("Enter your choice (1-3): ")
            angle = float(input("Enter the angle in degrees: "))
            if trig_choice == '1':
                print("Sine:", math.sin(math.radians(angle)))
            elif trig_choice == '2':
                print("Cosine:", math.cos(math.radians(angle)))
            elif trig_choice == '3':
                print("Tangent:", math.tan(math.radians(angle)))
            else:
                print("Invalid choice!")
        elif choice == '4':
            base = float(input("Enter the base: "))
            print("Natural logarithm:", math.log(base))
        elif choice == '5':
            print("Thank you for using the Scientific Calculator!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    scientific_calculator()
