from main import *

def cipher(data, flag):
    # Check the length of the data, if even or odd
    left, right = data[:len(data)//2], data[len(data)//2:]
    if flag == 1:
        if len(data) % 2 != 0:
            print("Invalid voucher regenerate again !")  
        # encrypt the data   
        l, r = round1(left, right)
        a, b = round2(l, r)
        # switch the left and right
        result = switch(a, b)
        print(result)
        return result
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
    left, right = right, left # switch left and right
    data = left + right # concat the two variables
    return data

def swap(code, pos1, pos2):  
    code = list(code)  # convert string to list of characters 
    code[pos1], code[pos2] = code[pos2], code[pos1] # swap the position of the characters 
    return ''.join(code) # convert list to string 

def  hash1(n):
    # swap string positions
    n = swap(n, 0, 2)
    return n

def  hash2(n):
    # swap string positions
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

# cipher(gen_voucher(122), 1)
cipher("7353131024706485", 0)

# cipher("6229162160415819", 1)
# cipher("480919510224841438", 0)