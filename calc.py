# Welcome message
print("Welcome to the Simple Calculator!")

while True:
    #displays options
    print("\n1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLICATION")
    print("4. DIVIDE")
    print("5. Quit")

    #get user choice
    choice = input("\nSelect a choice to perform: ")

    #check if user wants to quit
    if choice == '5':
        print("**********************************")
        print("Goodbye! Thanks for participating\n\tHave a great day!")
        print("**********************************")
        break  #exit the loop if user choose to quit 

    try:
        # to get numeric number from user to avoid valid entries
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        #perform the selected operation
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero!"
        else:
            result = "Invalid input. Please enter a number between 1 and 5"
          
        print(f"The Result is: {result}")       # Display the result

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")    #if user enters non-numeric values
