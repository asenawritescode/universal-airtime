from GenerateVoucher import Voucher
from RetryDecorator import Retry
from InvalidVoucher import InvalidVoucher

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
    
    def __init__(self,amount ,flag):
        """
        Parameters:
        ----------
        voucher : str
            The voucher code
        amount : int
            The value of the voucher
        flag : int
            The flag to indicate whether to encrypt or decrypt
        """
       
        self.amount = amount        
        self.voucher = Voucher(self.amount)
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
        if len(voucher) % 2 != 0:
            raise InvalidVoucher
        
        left, right = voucher.split_voucher()

        if flag == 1:
            l, r = self.round(left, right, 0 , 2)
            a, b = self.round(l, r, 1 , 2)
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

    def round(self, left, right, pos1, pos2):
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
        
        right_h = self.hash(right, pos1, pos2 = len(right)-1)
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
            pos = pow(2, i)
            d += str(data[pos])
        amount = d[::-1] #reverse string
        return amount
    
    # @Retry(tries=500, delay=0.5, exceptions=(InvalidVoucher))
    def run(self):
        """
        Runs the Feistel Cipher Algorithm
        """

        v = Voucher(self.amount)
        e, p, a = self.cipher(self.cipher(v, 1), 0)
        output = f'Voucher Code -> {e} \nPlain Code -> {p} \nAmount -> {a}'
        return output

f = FeistelCipher(198, 1)
print(f.run())