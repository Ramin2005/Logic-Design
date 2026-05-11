import re 

# dictionaries:

# dictionaries for base converting
# char -> int dict
# char_value = {'0' : 0, '1' : 1, '2' : 2, '3' : 3,
#             '4' : 4, '5' : 5, '6' : 6, '7' : 7,
#             '8' : 8, '9' : 9, 'A' : 10, 'B' : 11,
#             'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15,
#             'G' : 16, 'H' : 17, 'I' : 18, 'J' : 19,
#             'K' : 20, 'L' : 21, 'M' : 22, 'N' : 23,
#             'O' : 24, 'P' : 25, 'Q' : 26, 'R' : 27,
#             'S' : 28, 'T' : 29, 'U' : 30, 'V' : 31,
#             'W' : 32, 'X' : 33, 'Y' : 34, 'Z' : 35}
char_value = {chr(i): i - 48 for i in range(48, 58)}  # 0-9
char_value.update({chr(i): i - 55 for i in range(65, 91)}) # A-Z


# # int -> char dict
# value_char = {0 : '0', 1 : '1', 2 : '2', 3 : '3',
#             4 : '4', 5 : '5', 6 : '6', 7 : '7',
#             8 : '8', 9 : '9', 10 : 'A', 11 : 'B',
#             12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F',
#             16 : 'G', 17 : 'H', 18 : 'I', 19 : 'J',
#             20 : 'K', 21 : 'L', 22 : 'M', 23 : 'N',
#             24 : 'O', 25 : 'P', 26 : 'Q', 27 : 'R',
#             28 : 'S', 29 : 'T', 30 : 'U', 31 : 'V',
#             32 : 'W', 33 : 'X', 34 : 'Y', 35 : 'Z'}
value_char = {v: k for k, v in char_value.items()}

# dictionaries for bcd converting
# int -> bcd code dict
int_bcd = {0 : '0000', 1 : '0001', 2 : '0010', 3 : '0011', 4 : '0100',
           5 : '0101', 6 : '0110', 7 : '0111', 8 : '1000', 9 : '1001'}

# bcd code -> int dict
bcd_int = {'0000' : 0, '0001' : 1, '0010' : 2, '0011' : 3, '0100' : 4,
           '0101' : 5, '0110' : 6, '0111' : 7, '1000' : 8, '1001' : 9}


# mapping methods:
# base converting mapping methods: 

# method for mapping digits to integer values
def DigitToValue(digit: str) -> int:
    """
    returns value of digit.
    
    - d: target digit
    """
    
    # validation argument
    # get copy of upper case 
    d_copy = digit.upper()
    
    # checking:
    if not re.fullmatch(r'^[A-Z0-9]$', d_copy):
        raise RuntimeError("Method has been called with invalid digit")
    
    # returning result
    return char_value[d_copy]

# method for mapping integer values to digits
def ValueToDigit(value: int) -> str:
    """
    returns digit of value.
    
    - value: target value
    """
    
    
    # validation argument
    v = int(value)
    valid = 0 <= v <= 35
    
    if not valid:
        raise RuntimeError("Value must be between 0 to 35!")
    
    # returning result
    return value_char[v]


# bcd converting mapping methods: 

# method for mapping bcd code to decimal
def BCDToDecimal(bcd: str) -> int:
    """
    returns decimal value of BCD code.
    
    - bcd: target bcd code
    """
    
    # validation argument
    # get copy of upper case 
    bcd_copy = bcd.upper()
    
    # checking:
    if not re.fullmatch(r'^[01]{4}$', bcd_copy):
        raise RuntimeError("BCD code must be exactly 4 bits (0 or 1)")
    
    if bcd_copy not in bcd_int:
        raise RuntimeError("Invalid BCD code (valid codes: 0000 to 1001)")
    
    # returning result
    return bcd_int[bcd_copy]



# method for mapping decimal to bcd code
def DecimalToBCD(value: int) -> str:
    """
    returns BCD code of value.
    
    - v: target value
    """
    
    # validation argument
    v = int(value)
    valid = 0 <= v <= 9
    
    if not valid:
        raise RuntimeError("Value must be between 0 to 9!")
    
    # returning result
    return int_bcd[v]