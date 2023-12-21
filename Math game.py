print(" ")
print("Math game")
print(" ")
start = True
not_wrong = False
while True:  
    while start :
        start = False
        print("Choose a option by typing with a name or a character in braces: ")
        print("Addition(+), Subtraction (-), Multiplication (*), Division(/), Exponentiation(**), Square root(*/)" )   
        option1= str(input("Choose a option: "))
        
        if option1 == "+" or option1 == "Addition":
            print(" ")
            print("You choose Addition(+)") 
            right_answer = 0
            not_wrong=True
            wrnog_answer=0
            print(" ")
            amount = int(input("Choose amount of example: "))
            print(" ")
            for i in range(amount):
                    import random
                    number1 = random.randint(1, 100)
                    import random
                    number2 = random.randint(1, 100)
                    print(f"{number1} + {number2}=")
                    answer=input("Answer: ")
                    if int(number1) + int(number2) == int(answer):
                        print(" ")
                        print("Right answer!!")
                        print(" ")
                        right_answer += 1
                    else:
                        print(" ")
                        print(f"Wrong answer again, right answer was {number1 + number2}")
                        print(" ")
                        wrnog_answer += 1
            
                
                
                    

        
        

        
        
        elif option1 == "-" or option1 =="Subtraction":
                print(" ")
                print("You choose Subtraction (-)")
                print(" ")
                not_wrong=True
                right_answer = 0
                wrnog_answer=0
                amount = int(input("Choose amount of example: "))
                print(" ")
                for i in range(amount):
                    import random
                    number1 = random.randint(1, 100)
                    import random
                    number2 = random.randint(1, 100)
                    print(f"{number1} - {number2}=")
                    answer=input("Answer: ")
                    if int(number1) - int(number2) == int(answer):
                        print(" ")
                        print("Right answer!!")
                        print(" ")
                        right_answer += 1
                    else:
                        print(" ")
                        print(f"Wrong answer again, right answer was {number1 - number2}")
                        print(" ")
                        wrnog_answer += 1
                    
        
        
        
        
        
        
        elif option1 == "*" or option1 =="Multiplication":
            print(" ")
            print("You choose Multiplication (*)")
            print(" ")
            not_wrong=True
            right_answer = 0
            wrnog_answer=0
            amount = int(input("Choose amount of example: "))
            print(" ")
            for i in range(amount):
                    import random
                    number1 = random.randint(1, 100)
                    import random
                    number2 = random.randint(0, 10)
                    print(f"{number1} * {number2}=")
                    answer=input("Answer: ")
                    print(" ")
                    if int(number1) * int(number2) == int(answer):
                        print(" ")
                        print("Right answer!!")
                        print(" ")
                        right_answer += 1
                    else:
                        print(" ")
                        print(f"Wrong answer again, right answer was {number1 * number2}")
                        print(" ")
                        wrnog_answer += 1     
        
        
        
        
        
        
        
        elif option1 == "/" or option1 =="Division":
                print(" ")
                print("You choose Division(/) ")
                print(" ")
                not_wrong=True
                right_answer = 0
                wrnog_answer=0
                amount = int(input("Choose amount of example: "))
                print(" ")
                for i in range(amount): 
                    import random

                    def generate_numbers():
                        number1 = random.randint(1, 100)
                        number2 = random.randint(1, 10)
                        
                        return number1, number2

                    def generate_divisible_numbers():
                        while True:
                            number1, number2 = generate_numbers()
                            if number1 % number2 == 0:
                                return number1, number2
                    number1, number2 = generate_divisible_numbers()
                    print(f"{number1} / {number2}")
                    answer = float(input("Answer: "))
                    print(" ")
                    if int(number1) / int(number2) == int(answer):
                        print(" ")
                        print("Right answer!!")
                        print(" ")
                        right_answer += 1
                    else:
                        print(" ")
                        print(f"Wrong answer again, right answer was {number1 / number2}")
                        print(" ")
                        wrnog_answer += 1
        
        
        
        
        
        
        
        elif  option1 == "**" or option1 =="Exponentiation":
            print(" ")
            print("You choose Exponentiation(**) ")
            print(" ")
            not_wrong=True
            right_answer = 0
            wrnog_answer=0
            amount = int(input("Choose amount of example: "))
            print(" ")
            for i in range(amount):
                    import random
                    number1 = random.randint(1, 20)
                    import random
                    number2 = random.randint(0, 3)
                    print(f"{number1} ^ {number2}=")
                    answer=input("Answer: ")
                    print(" ")
                    if int(number1) ** int(number2) == int(answer):
                        print(" ")
                        print("Right answer!!")
                        print(" ")
                        right_answer += 1
                    else:
                        print(" ")
                        print(f"Wrong answer again, right answer was {number1 ** number2}")
                        print(" ")
                        wrnog_answer += 1
        
        
        
        
        
        
        
        elif option1 == "*/" or option1 =="Square root":
            print(" ")
            print("You choose Square root(*/) ")
            print(" ")
            not_wrong=True
            right_answer = 0
            wrnog_answer=0
            import random
            amount = int(input("Choose amount of example: "))
            print(" ")
            number1 =[1,4,9,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]
            for i in range(amount):
                    number=random.choice(number1)
                    print(" ")
                    print(f"√ {number}")
                    answer = int(input("Answer:"))
                    if number **(1/2) == int(answer):
                        print(" ")
                        print("Right answer!!")
                        print(" ")
                        right_answer += 1
                    else:
                        print(" ")
                        print(f"Wrong answer again, right answer was {number ** (1/2)}")
                        print(" ")
                        wrnog_answer += 1

        
        else:
            print(" ")
            print("Wrong choice!!")  
            print(" ")
            not_wrong = False
            start = True
        if not_wrong == True:
            print(" ")
            print("_______________________________")
            print(" ")
            print("You have:")
            print("_______________________________")
            print(" ")
            print(f"Right answer: {right_answer}")
            print(f"Wrong answer: {wrnog_answer}")
            print("_______________________________ ")
            print(" ")
            start = True