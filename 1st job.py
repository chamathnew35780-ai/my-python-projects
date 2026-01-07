while True:
    #get what operation to perform
    mark = input("what is the mark(+,-,/,*)")

    #check validity of operation or exit command
    if mark == "exit":
        break
    elif mark not in ["+","-","/","*"]:
        print("invalid operation, please enter +, -, /, * or 'exit' to quit")
        continue

    #get numbers from user
    no_1 = float(input("enter the 1st number"))
    no_2 = float(input("enter the 2nd number"))

    #perform calculation based on operation
    if mark=="+":
        output = no_1 + no_2
    elif mark == "-":
        output = no_1 - no_2
    elif mark == "/":
        if no_2 == 0:
            output = "undefined (cannot divide by zero)"
        else:
            output = no_1/no_2
    elif mark == "*":
        output = no_1 * no_2
        
#display result
    print ("answer:" ,round(output, 2))
