from main import *

def bin_slice(bin_data):
    r = bin(bin_data)[2:]
    return r

def bin_to_decimal(bin_data):
    # Loop over the bin_data array and convert to decimal
    r = []
    for i in range(len(bin_data)):
        r.append(int(bin_data[i], 2))
    
    return print(''.join(map(str, r)))

def convert_to_binary(n):
    # convert the number to binary
    return list(map(bin_slice,bytearray(n, 'utf8')))

def cipher(data, flag):
    # Check the length of the data, if even or odd
    data = convert_to_binary(data)
    
    left, right = data[:len(data)//2], data[len(data)//2:]

    if flag == 1:
        if len(data) % 2 != 0:
            print("Invalid voucher regenerate again !")
            
        # encrypt the data   
        l, r = round1(left, right)
        a, b = round2(l, r)
        # switch the left and right
        return switch(a, b)
    
    elif flag == 0:
        # decrypt the data        
        l, r = round2(left, right)
        l, r = round1(l, r)
        # switch the left and right
        result = switch(l, r)
        print(result)
        return result
    else:
        print("Invalid flag")
        return
    
# switch them up 
def switch(left, right):
    # switch left and right
    left, right = right, left
    # return concat the two variables
    # data = str(left) + str(right)
    print(left + right)
    return bin_to_decimal(left + right)

def swap(code, pos1, pos2):  
    # swap the position of the characters 
    code[pos1], code[pos2] = code[pos2], code[pos1] 
    # convert list to string 
    return code

def xor(a,b):
    c = []
    e = []
    print(len(a))
    print(b)
    for i in range(len(a)):
        for j in range(len(b[i])):
            d = ord(a[i][j]) ^ ord(b[i][j])
            e.append(d)
        f = ''.join(map(str, e))
        c.append(f)
        e.clear()
    return c

def  hash1(n):
    # swap string positions
    n = swap(n, 0, 2)
    return n

def  hash2(n):
    # swap string positions
    n = swap(n, 1, (len(n)-1))
    return n

# function round 1
def round1(left, right):
    # right gets into function
    right_h = hash1(right)

    # copy right to left
    left_temp = right

    # XOR right_h and left
    new_right = xor(right_h, left)

    # assign the right to the new left 
    new_left = left_temp
    # return 
    return new_left, new_right

def round2(new_left, new_right):
    # right gets into function
    right_h = hash2(new_right)
    
    # copy right to left
    left_temp = new_right
    
    # XOR right_h and left
    right = xor(right_h, new_left)

    left = left_temp    
    # return 
    return left, right

# cipher(gen_voucher(122), 1)

# cipher("0224185899658401", 1)
# these are 27 in number (14,13)
cipher("48485052495653586911191251", 0)