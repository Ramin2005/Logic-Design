import mapper

#converter functions:

#grey to any number in base between 2 and 36
def number_to_grey_code(aa, first_base=2) -> str:
    assert 2 <= first_base <= 36, "The first base must be between 2 and 36!"
    
    binary_code = str(aa)
    assert (binary_code.find(".") < 0), "The first number must be integer!"
    
     
    if first_base != 2:
        binary_code = base_converter(binary_code, 2, first_base=first_base, floating_point=0)
    
    out = binary_code[0]
    for i in range(1, len(binary_code)):
        temp = '0'
        if (int(binary_code[i]) ^ int(binary_code[i - 1])):
            temp = '1'
        out = out + temp
        
    return out

#grey to any number in base between 2 and 36
def grey_code_to_number(grey: str, base_out=2) -> str:
    assert 2 <= base_out <= 36, "The base must be between 2 and 36!"
    
    grey_code = grey
    
    count_0 = grey_code.count('0')
    count_1 = grey_code.count('1')
    
    assert (count_0 + count_1) == len(grey_code), "Invalid grey code entered!"
    
    out = grey_code[0]
    for i in range(1, len(grey_code)):
        temp = '0'
        if (int(grey_code[i]) ^ int(out[i - 1])):
            temp = '1'
        out = out + temp

    return base_converter(out, base_out, first_base=2, floating_point=0)

#decimal to bcd converter
def integer_to_bcd(aa: int) -> str:
    assert aa > -1, "The entered value must be greater than or equal to zero!"
    
    a = str(aa)
    
    out = ""
    
    for i in range(len(a)):
        out = out + mapper.DecimalToBCD(int(a[i]))
        
    return out

#bcd to integer converter
def bcd_to_integer(aa: str) -> int:
    
    a = str(aa)
    
    assert len(a) % 4 == 0, "Invalid bcd code entered!"
    
    count_0 = a.count('0')
    count_1 = a.count('1')
    
    assert (count_0 + count_1) == len(a), "Invalid bcd code entered!"
    
    out = 0;
    for i in range(0, len(a), 4):
        
        temp = a[i: i + 4]
        
        out = 10 * out + mapper.BCDToDecimal(temp)
        
    return out

# to base ten function
def to_base_ten(aa, first_base: int) -> float:
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
        
        
        assert mapper.DigitToValue(temp) < first_base, "invalid number entered!"
        
        out += (mapper.DigitToValue(temp)) * (first_base **  (int_count - 1 -i))
        
    if(int_count < length):
        for i in range(int_count + 1, length):
        
            temp = a[i]
        
            assert mapper.DigitToValue(temp) < first_base, "invalid number entered!"
        
            out += (mapper.DigitToValue(temp)) * (first_base **  (int_count - i))
        
    return out
    
    
def base_converter(aa: str | int | float, second_base: int, first_base=10, floating_point=10) -> str:
    """
    base conversion function; This function can convert numbers in bases between 2 and 36.
    """
    
    assert 2 <= first_base <= 36, "The first base must be between 2 and 36!"
    assert 2 <= second_base <= 36, "The second base must be between 2 and 36!"
    
    assert floating_point < 13 ,"The number of decimal digits must be less than 13!"
    
    a = aa
    
    if first_base != 10:
        a = to_base_ten(a, first_base)
    else:
        a = float(a)
        
    fractional = a % 1
    a = int(a)
    
    out = ''
    
    temp = a % second_base
    a = a // second_base
    
    out = out + str(mapper.ValueToDigit(temp))
    
    while a != 0:
        temp = a % second_base
        a = a // second_base
    
        out = str(mapper.ValueToDigit(temp)) + out 
    
    if floating_point > 0 and fractional:
        
        out = out + '.'
        
        counter = 1
        
        while counter <= floating_point and fractional > 1e-13:
            counter += 1
            
            temp = int(fractional * second_base)
            fractional = fractional * second_base - temp
            
            out = out + str(mapper.ValueToDigit(temp))
    
    return out
