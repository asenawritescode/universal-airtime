from nanoid import generate as g

class Voucher:
    """
    Voucher Generation Implementation

    Attributes:
    ----------
    amount: int
        The value of the voucher
    code: str
        The voucher code
    
    Methods:
    -------
    gen_voucher(amount) -> str:
        Generates a voucher code of the specified value
    
    add_value(amount, voucher)-> str:
        Embed voucher value to the geneated voucher code
    
    """

    def __init__(self, amount):
        """
        Parameters:
        ----------
        amount: int
            The value of the voucher
        """

        self.amount = amount
        self.code = self.gen_voucher(self.amount)

    def __str__(self):  
        """
        Returns:
        -------
        code : str
        """

        return self.code.__str__()
    
    def __repr__(self) -> str:
        """
        Returns:
        -------
        Voucher object : str
        """

        return f'Voucher( {self.amount} , {self.code} )'
    
    def __len__(self) -> int:
        """
        Returns:
        -------
        length : int
        """

        return len(self.code)
    
    def add_value(self, voucher: int, amount: int) -> str:
        """
        Embed voucher value to the geneated voucher code

        Parameters:
        ----------
        voucher: int
            The voucher code
        amount: int
            The value of the voucher
        
        Returns:
        ------
        voucher : str
        """
        n = int(str(len(amount)))
        i = n - 1
        for d in amount:
            pos = pow(2, i)
            voucher[pos] = d # Embed the amount to the voucher
            i-=1
        voucher[15] = n # assign amount value len at position 15
        
        voucher = ''.join(map(str, voucher))
        
        return voucher
    
    def gen_voucher(self, amount: int) -> str:
        """
        Generates a voucher code of the specified value

        Parameters:
        ----------
        amount: int
            The value of the voucher
        
    Raises:
        ------
        ValueError
            If amount is not in the range 10-1000
        
        Returns:
        -------
        code : str
        """

        if amount < 10 or amount > 1000: # check if amount is in valid range (10-1000)
            raise ValueError("Invalid amount ("+amount.__str__()+") should be between 10 and 1000")

        code = g("0123456789", 16) # Generate a random 16 digit number
        v_str = list(code) 
        a_str = list(amount.__str__()) 
        v_digits = [int(digit) for digit in v_str] 
        a_digits = [int(digit) for digit in a_str] 

        voucher = self.add_value(v_digits, a_digits) 

        return voucher