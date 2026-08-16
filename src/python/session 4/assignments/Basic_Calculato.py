def Basic_Cal():
    '''
    This is a basic calculator
    
    '''
    
    L1 = ["1", "2", "3", "4", "exit"]
    while True:
        check = False
        operation = input("Select an operation:\n1-addition +\n2-subtraction -\n3-multiplication *\n4-division /\n" \
                "Enter your chose (1/2/3/4) or ( exit ) to quit:").lower()
        
        if operation == "exit":
            return print("Thank you for you time.")
        
        for i in L1:
            if i==operation:
                check = True
            
        if check:
            num1 = int(input("Enter First Number :"))
            num2 = int(input("Enter Second Number :"))
            
            while operation == "4" and num2 == 0:
                num2 = int(input("Number 2 can't be zero for division. Please enter it again: "))
                
            if operation == "1":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operation == "2":
                result = num1 - num2 
                print(f"{num1} - {num2} = {result}") 
            elif operation == "3":
                result = num1 * num2  
                print(f"{num1} * {num2} = {result}") 
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")    
        else :
            print("I am sorry, that is not a valid operation.")  
                 