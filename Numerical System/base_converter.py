char_num = {'0' : 0, '1' : 1, '2' : 2, '3' : 3,
            '4' : 4, '5' : 5, '6' : 6, '7' : 7,
            '8' : 8, '9' : 9, 'A' : 10, 'B' : 11,
            'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

num_char = {0 : '0', 1 : '1', 2 : '2', 3 : '3',
            4 : '4', 5 : '5', 6 : '6', 7 : '7',
            8 : '8', 9 : '9', 10 : 'A', 11 : 'B',
            12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}

bcd = {0 : '0000', 1 : '0001', 2 : '0010', 3 : '0011', 4 : '0100',
       5 : '0101', 6 : '0110', 7 : '0111', 8 : '1000', 9 : '1001'}


# to base ten function
def to_base_ten(aa, base_a) -> float:
    out = 0
    
    a = str(aa)
    
    point = a.find('.')
    length = len(a)
    int_count = point
    float_count = (length - point - 1)
    #43210.123 9
    for i in range(int_count):
        
        temp = a[i]
        
        assert char_num[temp] < base_a, "invalid number entered!"
        
        out += (char_num[temp]) * (base_a **  (int_count - 1 -i))
    
    for i in range(int_count + 1, length):
        
        temp = a[i]
        
        assert char_num[temp] < base_a, "invalid number entered!"
        
        out += (char_num[temp]) * (base_a **  (int_count - i))
        
    return out
        
    

def base_a_to_base_b(aa, second_base, first_base=10, floating_point=10) -> str:
    
    assert floating_point < 13 ,"floating point should be less than 13!"
    
    a = aa
    floating = 0.0
    
    if first_base != 10:
        a = to_base_ten(a, base_a)
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
    
    if floating != 0:
        
        out = out + '.'
        
        counter = 1
        
        while counter <= floating_point and floating > 1e-13:
            counter += 1
            
            temp = floating * second_base // 1
            floating = floating * second_base - temp
            
            out = out + str(num_char[temp])
    
    return out
    
    

aa = input("Enter the number: ")
base_a = int(input("Enter the first base: "))
base_b = int(input("Enter the second base: "))

print(base_a_to_base_b(aa, base_b, base_a))