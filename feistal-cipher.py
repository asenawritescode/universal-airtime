# data = "123456789"
# data = "123455559"
data = "32921780431"

# divide the data into two parts using slicing 
left, right = data[:len(data)//2], data[len(data)//2:]
print("Start: /n")
print("Left: ", left)
print("Right: ", right)
print("End: ")

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
    left = int(left)
    right = int(right)
    # right gets into function
    right_h = int(hash1(right))
    # copy right to left
    left_temp = right
    # XOR right_h and left
    new_right = right_h ^ left
    new_left = left_temp
    
    # return left and right, call function round2
    return round2(new_left, new_right)

def round2(new_left, new_right):
    # right gets into function
    
    right_h = int(hash2(str(new_right)))
    # copy right to left
    left_temp = new_right
    # XOR right_h and left
    right = right_h ^ new_left
    left = left_temp    
    # return print("Left: ", left, "Right: ", right)
    return switch(left, right)


print(round1(left, right))



