from GenerateVoucher import gen_voucher
from RetryDecorator import Retry
from InvalidVoucher import InvalidVoucher
    
def cipher(data, flag):
    
    if len(data) % 2 != 0:     # Check the length of the data, if even or odd
        raise InvalidVoucher 
    if len(data) > 16:
        raise InvalidVoucher
    
    left, right = data[:len(data)//2], data[len(data)//2:]
    
    if flag == 1: # encrypt the data   
        l, r = round1(left, right)
        a, b = round2(l, r)
        result = switch(a, b) # switch the left and right
        # print("encrypted - >",result)
        return result
    
    elif flag == 0: # decrypt the data        
        l, r = round2(left, right)
        l, r = round1(l, r)
        result = switch(l, r) # switch the left and right
        amount = get_amount(result)
        # print("decrypted - >",result)
        return result, amount
    else:
        raise UserWarning("Error Invalid flag")

def get_amount(data):
    # data = list(data)
    d = ""
    end = int(data[15])
    for i in range(0, end):
        pos = pow(2, i)
        d += str(data[pos])
    # print(reverse(d))
    return reverse(d)

def reverse(x):
  return x[::-1]

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
    return new_left, new_right  

def round2(left, right):
    right_h = hash2(right)
    left_temp = right
    new_right = ""
    for i in range(len(left)):
        new_right += str(ord(right_h[i]) ^ ord(left[i]))
    new_left = left_temp
    return new_left, new_right

# cipher(gen_voucher(10), 1)
@Retry(tries=50, delay=0.1, exceptions=(InvalidVoucher))
def run():
    # cipher(cipher(gen_voucher(120), 1), 0)
    # encry_code = 6720130457122050
    # plain_code = 6020130337323353 - 120
    