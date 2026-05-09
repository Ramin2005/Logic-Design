import code_and_number_converter
import os

n = ""
b1 = -1
b2 = -1

while True:
    n = -1
    
    os.system('cls')
    print("Enter negative number to exit program.")
    n = input("Enter number: ")

    if n.startswith('-'):
        break   

            
    while b1 < 2 and b1 > 37:
        print("Base must be between 2 to 36.")
        
        try:
            b1 = int(input("Enter first base of number: "))

        except ValueError:
            os.system('cls')
            print("Enter valid number for first base!")
            input("Press enter to continue. ")
            os.system('cls')
            
    while b2 < 2 and b2 > 37:
        print("Base must be between 2 to 36.")
        
        try:
            b2= int(input("Enter second base: "))

        except ValueError:
            os.system('cls')
            print("Enter valid number for second base!")
            input("Press enter to continue. ")
            os.system('cls')
            

    os.system('cls')
    
    try:   
        print(f"{n} from base {b1} to base {b2}:",code_and_number_converter.base_converter(n, b2, first_base=b1, floating_point=12))
    except:
        print("Entered number is invalid!")

    input("Press enter to restart.")