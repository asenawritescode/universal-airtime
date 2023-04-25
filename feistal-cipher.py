data = "123456789"

# divide the data into two parts using slicing 
left, right = data[:len(data)//2], data[len(data)//2:]
print("Start: /n")
print("Left: ", left)
print("Right: ", right)

# switch them up 
def switch(left, right):
    # switch left and right
    left, right = right, left

    # concat the two variables
    data = str(left) + str(right)

    return data

def  hash1(n):
    # transposing the string
    return n

# function round 1
def round1(left, right):
    left = int(left)
    right = int(right)
    # right gets into function
    right_h = hash1(right)
    # copy right to left
    left_temp = right
    # XOR right_h and left
    right = right_h ^ left
    left = left_temp
    
    # return left and right, call function round2
    return round2(left, right)


def round2(left, right):
    # right gets into function
    
    right_h = hash1(right)
    # copy right to left
    left_temp = right
    # XOR right_h and left
    right = right_h ^ left
    left = left_temp    
    return switch(left, right)


print(round1(left, right))



