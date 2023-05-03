from GenerateVoucher import gen_voucher
from RetryDecorator import Retry
from InvalidVoucher import InvalidVoucher
    
def cipher(data, flag):
    
    if len(data) % 2 != 0:     # Check the length of the data, if even or odd
        raise InvalidVoucher 
    
    left, right = data[:len(data)//2], data[len(data)//2:]
    
    if flag == 1: # encrypt the data   
        l, r = round1(left, right)
        a, b = round2(l, r)
        result = switch(a, b) # switch the left and right
        print(result)
        return result
    
    elif flag == 0: # decrypt the data        
        l, r = round2(left, right)
        l, r = round1(l, r)
        result = switch(l, r) # switch the left and right
        print(result)
        return result
    else:
        raise UserWarning("Error Invalid flag")
            
def switch(left, right):
    left, right = right, left # switch left and right
    data = left + right # concat the two variables
    return data

def swap(code, pos1, pos2):  
    code = list(code)  # convert string to list of characters 
    code[pos1], code[pos2] = code[pos2], code[pos1] # swap the position of the characters 
    return ''.join(code) # convert list to string 

def  hash1(n):  # swap string positions
    n = swap(n, 0, 2)
    return n

def  hash2(n):  # swap string positions
    n = swap(n, 1, (len(n)-1))
    return n

def round1(left, right):
    right_h = hash1(right)
    left_temp = right  
    new_right = ""
    for i in range(len(left)):
        new_right += str(ord(right_h[i]) ^ ord(left[i]))
    new_left = left_temp
    print("1-",new_left, new_right)
    return new_left, new_right  

def round2(left, right):
    right_h = hash2(right)
    left_temp = right
    new_right = ""
    for i in range(len(left)):
        new_right += str(ord(right_h[i]) ^ ord(left[i]))
    new_left = left_temp
    print("2-",new_left, new_right)
    return new_left, new_right

# cipher(gen_voucher(10), 1)
@Retry(tries=100, delay=0.1, exceptions=(InvalidVoucher))
def run():
    cipher(cipher(gen_voucher(10), 1), 0) 