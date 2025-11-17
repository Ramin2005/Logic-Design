#dicts:

#char -> int dict
char_num = {'0' : 0, '1' : 1, '2' : 2, '3' : 3,
            '4' : 4, '5' : 5, '6' : 6, '7' : 7,
            '8' : 8, '9' : 9, 'A' : 10, 'B' : 11,
            'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15,
            'G' : 16, 'H' : 17, 'I' : 18, 'J' : 19,
            'K' : 20, 'L' : 21, 'M' : 22, 'N' : 23,
            'O' : 24, 'P' : 25, 'Q' : 26, 'R' : 27,
            'S' : 28, 'T' : 29, 'U' : 30, 'V' : 31,
            'W' : 32, 'X' : 33, 'Y' : 34, 'Z' : 35}

#int -> char dict
num_char = {0 : '0', 1 : '1', 2 : '2', 3 : '3',
            4 : '4', 5 : '5', 6 : '6', 7 : '7',
            8 : '8', 9 : '9', 10 : 'A', 11 : 'B',
            12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F',
            16 : 'G', 17 : 'H', 18 : 'I', 19 : 'J',
            20 : 'K', 21 : 'L', 22 : 'M', 23 : 'N',
            24 : 'O', 25 : 'P', 26 : 'Q', 27 : 'R',
            28 : 'S', 29 : 'T', 30 : 'U', 31 : 'V',
            32 : 'W', 33 : 'X', 34 : 'Y', 35 : 'Z'}

#int -> bcd code dict
int_bcd = {0 : '0000', 1 : '0001', 2 : '0010', 3 : '0011', 4 : '0100',
           5 : '0101', 6 : '0110', 7 : '0111', 8 : '1000', 9 : '1001'}

#bcd code -> int dict
bcd_int = {'0000' : 0, '0001' : 1, '0010' : 2, '0011' : 3, '0100' : 4,
           '0101' : 5, '0110' : 6, '0111' : 7, '1000' : 8, '1001' : 9}

#converter functions:

#grey to any number in base between 2 and 36
def base_a_to_grey(aa, base_aa) -> str:
    assert (base_aa < 37 & base_aa > 1), "The base must be between 2 and 36!"
    
    a = str(aa)
    assert (a.find(".") < 0), "The first number must be integer!"
    
    binary_code = base_converter(a, 2, first_base=base_aa, floating_point=0)
    
    return ""

#grey to any number in base between 2 and 36
def grey_to_base_a(grey, base_aa) -> str:
    assert (base_aa < 37 & base_aa > 1), "The base must be between 2 and 36!"
    return ""

#decimal to bcd converter
def integer_to_bcd(aa) -> str:
    assert type(aa) == int, "iThe input must be an integer!"
    assert aa > -1, "The entered value must be greater than or equal to zero!"
    
    a = str(aa)
    
    out = ""
    
    for i in range(len(a)):
        out = out + (int_bcd[int(a[i])])
        
    return out

#bcd to integer converter
def bcd_to_integer(aa) -> int:
    
    a = str(aa)
    
    assert len(a) % 4 == 0, "Invalid bcd code entered!"
    
    count_0 = a.count('0')
    count_1 = a.count('1')
    
    assert (count_0 + count_1) == len(a), "Invalid bcd code entered!"
    
    out = 0;
    for i in range(0, len(a), 4):
        
        temp = a[i: i + 4]
        
        out = 10 * out + bcd_int[temp]
        
    return out

# to base ten function
def to_base_ten(aa, base_aa) -> float:
    out = 0
    
    a = str(aa)
    
    point = a.find('.')
    length = len(a)
    
    if point > -1:
        int_count = point
    else: 
        int_count = length
        
    for i in range(int_count):
        
        temp = a[i]
        
        
        assert char_num[temp] < base_aa, "invalid number entered!"
        
        out += (char_num[temp]) * (base_aa **  (int_count - 1 -i))
        
    if(int_count < length):
        for i in range(int_count + 1, length):
        
            temp = a[i]
        
            assert char_num[temp] < base_aa, "invalid number entered!"
        
            out += (char_num[temp]) * (base_aa **  (int_count - i))
        
    return out
    
#base conversion function; This function can convert numbers in bases between 2 and 36.
def base_converter(aa, second_base, first_base=10, floating_point=10) -> str:
    assert (first_base < 37 & first_base > 1), "The first base must be between 2 and 36!"
    assert (second_base < 37 & second_base > 1), "The second base must be between 2 and 36!"
    
    assert floating_point < 13 ,"The number of decimal digits must be less than 13!"
    
    a = aa
    floating = 0.0
    
    if first_base != 10:
        a = to_base_ten(a, first_base)
    else:
        a = float(a)
        
    floating = a % 1
    a = int(a)
    
    out = ''
    
    temp = a % second_base
    a = a // second_base
    
    out = out + str(num_char[temp])
    
    while a != 0:
        temp = a % second_base
        a = a // second_base
    
        out = str(num_char[temp]) + out 
    
    if floating != 0 & floating_point > 0:
        
        out = out + '.'
        
        counter = 1
        
        while counter <= floating_point and floating > 1e-13:
            counter += 1
            
            temp = floating * second_base // 1
            floating = floating * second_base - temp
            
            out = out + str(num_char[temp])
    
    return out
