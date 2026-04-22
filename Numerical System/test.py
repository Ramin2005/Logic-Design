import code_and_number_converter
import os

os.system('cls')
n = input("Enter number: ")
b1 = int(input("Enter first base of number: "))
b2 = int(input("Enter second base: "))

print(code_and_number_converter.base_converter(n, b2, first_base=b1, floating_point=12))