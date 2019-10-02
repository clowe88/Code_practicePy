import operator

def main(): #menu goes here
    opt_list = ["accept_and_store", "calculator", "print_string", "num_compare", "remove_letter", "exit"]

    print ("Select option")
    print ("1\tAccept and Store")
    print ("2\tCalculator")
    print ("3\tPrint Stored String")
    print ("4\tNumber Comaparison")
    print ("5\tLetter Remover")
    print ("6\tExit")

    opt_choice = int(input("Selection: "))
    opt_choice -= 1
    globals()[opt_list[opt_choice]]()
    return

def accept_and_store(): #accept and store a string
    global saved_string
    saved_string = str(input("Input a string: "))
    main()
    return

def calculator(): # basic calculator
    symbol_dict = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv, "%":operator.mod}

    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    symbol = input("Enter mathmatical symbol: ")
    result = int()
    
    print (symbol_dict[symbol](num_1, num_2))
    
    main()
    return

def print_string(): #print previously stored string
    print(saved_string)
    main()
    return

def num_compare(): #compare 2 numbers return larger number
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if num1 > num2:
        return num1
    elif num2 > num1: 
        return num2
    else:
        print ("Equal")

    main()

def remove_letter(): #remove selected letter from a string
    string_remove = input("Enter the string you wish to remove a letter from: ")
    letter_remove = input("Enter the letter you wish to remove from the string: ")
    letter_remove = letter_remove(0)
    print(string_remove.replace(letter_remove, ""))
    main()
    return

def exit():
    return

main()