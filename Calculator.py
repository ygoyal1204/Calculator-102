  
print("Welcome to this Calculator!")
print("Press '1' to do Addition, '2' to do Subtraction, '3' to do Multiplication, '4' to do Division.")

choice =   int(input("Choose what you want to do: "))
num1   =   int(input("Enter The First Number: "))
num2   =   int(input("Enter The Second Number: "))

add = float(num1 + num2)
subtract =float(num1 - num2)
multiply = float(num1 * num2)
divide = float(num1 / num2)

if choice == 1:
    print("The sun is ", add)
elif choice == 2:
    print("The difference is ",subtract)
elif choice == 3:
    print("Your product is ",multiply)
elif choice == 4:
    print("Your quotient is ",divide)
else:
    print("The choice is not valid.")  
