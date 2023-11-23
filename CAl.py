while True:
    print("1 Add")
    print("2 Minus")
    print("3 Devid")
    print("4 Multiply")
    print("press q for exit")
    choice = 0
    choices = ["1", "2", "3", "4", "q", "Q"]
    while choice not in choices:
        choice = input("What do you whant to do?")
    if choice == "q":
        break
    
    



    def add(num1, num2):
        result = num1 + num2
        print(str(num1) + " + " + str(num2) + " = " + str(result))

    def minus(num1, num2):
        result = num1 - num2
        print(str(num1) + " - " + str(num2) + " = " + str(result))

    def devid(num1, num2):
        result = num1 / num2
        print(str(num1) + "  / " + str(num2) + " = " + str(result))

    def multiply(num1, num2):
        result = num1 * num2
        print(str(num1) + " * " + str(num2) + " = " + str(result))

    n1 = input("Insert your first number: ")
    n2 = input("Insert your second number: ")
    n1 = float(n1)
    n2 = float(n2)

    if choice == "1":
        add(n1, n2)
    if choice == "2":
        minus(n1, n2)
    if choice == "3":
        devid(n1, n2)
    if choice == "4":
        multiply(n1, n2)
