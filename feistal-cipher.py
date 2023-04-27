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
    # switch left and right
    left, right = right, left
    # concat the two variables
    data = str(left) + str(right)
    return data

def swap(code, pos1, pos2): 
    # convert string to list of characters 
    code = list(str(code)) 
    # swap the position of the characters 
    code[pos1], code[pos2] = code[pos2], code[pos1] 
    # convert list to string 
    return ''.join(code)

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
    print(right_h, "right_h")
    # copy right to left
    left_temp = right
    # XOR right_h and left
    new_right_list = [(ord(a) ^ ord(b)) for a, b in zip(right_h, left)]
    new_right = ''.join(map(str, new_right_list))
    # assign the right to the new left 
    new_left = left_temp
    # return left and right, call function round2
    return new_left, new_right

def round2(new_left, new_right):
    # right gets into function
    
    right_h = hash2(new_right)
    # copy right to left
    left_temp = new_right
    # XOR right_h and left
    # right = right_h ^ int(new_left)
    right_list = [(ord(a) ^ ord(b)) for a, b in zip(right_h, new_left)]
    print(right_list, "right_list")
    right = ''.join(map(str, right_list))
    left = left_temp    
    # return print("Left: ", left, "Right: ", right)
    return left, right

# cipher(gen_voucher(122), 1)
# cipher("0229162160415819", 1)
# cipher("3044746138357038", 0)
# cipher("7226132742576398", 1)
# cipher("673613892061701115", 0)
cipher("1234567890", 0)

# cipher("1234567890", 1)