from GenerateVoucher import Voucher
from RetryDecorator import Retry
from InvalidVoucher import InvalidVoucher
    
def cipher(data, flag):
    
    left, right = data.split_voucher() # split the data into two halves
    print("left ->",left)
    print("right ->",right)

    if len(data) % 2 != 0:     # Check the length of the data, if even or odd
        raise InvalidVoucher 
    if len(data) > 16:
        raise InvalidVoucher
    
    
    if flag == 1: # encrypt the data   
        l, r = round1(left, right)
        a, b = round2(l, r)
        result = switch(a, b) # switch the left and right
        return result
    
    elif flag == 0: # decrypt the data
        e = left + right
        # print("Encrypted - >",e)        
        l, r = round2(left, right)
        l, r = round1(l, r)
        result = switch(l, r) # switch the left and right
        amount = get_amount(result)
        # print("decrypted - >",result)
        return e, result, amount
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

@Retry(tries=500, delay=0.5, exceptions=(InvalidVoucher))
def run():
    # encry_code = 6720130457122050
    # plain_code = 6020130337323353 - 120
    a = Voucher(1000)
    e, p, a = cipher(cipher(a, 1), 0)
    output  = f'Voucher Code -> {e} \nPlain Code -> {p} \nAmount -> {a}'
    print(output)
    return output

run()



class FeistelCipher:
    """
    The Feistel Cipher Implementation
    
    Attributes:
    ----------
    voucher : str
        The voucher code
    flag : int
        The flag to indicate whether to encrypt or decrypt
    
    Methods:
    -------
    cipher(self, voucher: str, flag: int) -> str
        Encrypts or decrypts the voucher code
    
    round(self, left: str, right: str) -> list
        Single round of the Feistel Cipher Algorithm
    
    switch(self, left: str, right: str) -> str
        Switches the left and right halves of the voucher code
    
    swap(self, code: str, pos1: int, pos2: int) -> str
        Swaps the positions of two characters in the voucher code
    
    hash(self, n: str, pos1, pos2) -> str
        Swap some string positions in the voucher code
    
    get_amount(self, data: str) -> str
        Gets the amount from the voucher plain code
    
    run(self) -> str
        Runs the Feistel Cipher Algorithm
    
    
    """
    
    def __init__(self, voucher, flag):
        """
        Parameters:
        ----------
        voucher : str
            The voucher code
        flag : int
            The flag to indicate whether to encrypt or decrypt
        """
       
        self.voucher = voucher
        self.flag = flag

    def __str__(self) -> str:
        pass
    
    def cipher(self, voucher, flag):
        """
        Encrypts or decrypts the voucher code
        
        Parameters:
        ----------
        voucher : str
            The voucher code
        flag : int
            The flag to indicate whether to encrypt or decrypt
        
        Raises:
        ------
        InvalidVoucher
            If the voucher code is invalid
        UserWarning
            If the flag is invalid
        
        Returns:
        -------
        str
            The encrypted or decrypted voucher code
        """
        
        left, right = voucher.split_voucher()

        if len() % 2 != 2:
            raise InvalidVoucher

        if flag == 1:
            l, r = self.round(left, right)
            a, b = self.round(l, r)
            result = self.switch(a, b)
            return result
        elif flag == 0:
            e = left + right
            l, r = self.round(left, right)
            l, r = self.round(l, r)
            result = self.switch(l, r)
            amount = self.get_amount(result)
            return e, result, amount
        else:
            raise UserWarning("Error Invalid flag")

    def round(self, left, right):
        """
        Single round of the Feistel Cipher Algorithm
        
        Parameters:
        ----------
        left : str
            The left half of the voucher code
        right : str
            The right half of the voucher code
        
        Returns:
        -------
        list
            The left and right halves of the voucher code
        """
        
        right_h = self.hash_first(right)
        left_temp = right
        new_right = ""
        for i in range(len(left)):
            new_right += str(ord(right_h[i]) ^ ord(left[i]))
        new_left = left_temp
        return new_left, new_right
    
    def switch(self, left, right):
        """
        Switches the left and right halves of the voucher code
        
        Parameters:
        ----------
        left : str
            The left half of the voucher code
        right : str
            The right half of the voucher code
        
        Returns:
        -------
        str
            The switched voucher code
        """
        
        left, right = right, left
        data = left + right
        return data
    
    def swap(self, code, pos1, pos2):
        """
        Swaps the positions of two characters in the voucher code
        
        Parameters:
        ----------
        code : str
            The voucher code
        pos1 : int
            The first position
        pos2 : int
            The second position
        
        Returns:
        -------
        str
            The voucher code with the swapped characters
        """
        
        code = list(code)
        code[pos1], code[pos2] = code[pos2], code[pos1]
        return ''.join(code)
    
    def hash(self, n, pos1, pos2):
        """
        Swap some string positions in the voucher code
        
        Parameters:
        ----------
        n : str
            The voucher code
        
        pos1 : int
            The first position
        
        pos2 : int
            The second position

        Returns:
        -------
        str
            The voucher code with swapped characters
        """
        
        n = self.swap(n, pos1 , pos2)
        return n
    
    def get_amount(self, data):
        """
        Gets the amount from the voucher plain code
        
        Parameters:
        ----------
        data : str
            The voucher plain code
        
        Returns:
        -------
        str
            The amount
        """
        end = int(data[15])
        d = ""
        for i in range (0, end):
            pos = pow(2,1)
            d += str(data[pos])
        amount = data[::-1] #reverse string
        return amount
    
    def run(self, amount):
        """
        Runs the Feistel Cipher Algorithm
        """

        v = Voucher(amount)
        e, p, a = cipher(cipher(v, 1), 0)
        output = f'Voucher Code -> {e} \nPlain Code -> {p} \nAmount -> {a}'
        return output
