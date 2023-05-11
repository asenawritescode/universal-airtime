"""Module to run voucher code through Feistel Algorithm for encryption and decryption."""
from generate_voucher import Voucher
from invalid_voucher import InvalidVoucher
from split_voucher import split_voucher


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

    """

    def __init__(self, amount, flag):
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
        left, right = split_voucher(voucher)

        if len(voucher) % 2 != 0:
            raise InvalidVoucher

        if len(voucher) > 16:
            raise InvalidVoucher

        if flag == 1:
            l, r = self.round(left, right, 0, 2)
            a, b = self.round(l, r, 1, 2)
            result = self.switch(a, b)
            return result
        elif flag == 0:
            original_str = left + right
            left_r, right_r = self.round(left, right, 1, 2)
            left, right = self.round(left_r, right_r, 0, 2)
            result = self.switch(left, right)
            amount = self.get_amount(result)
            return original_str, result, amount
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

        right_h = self.hash(right, pos1, pos2=len(right) - 1)
        left_temp = right
        new_right = ""
        len_left = len(left)
        for i in range(len_left):
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
        return "".join(code)

    def hash(self, voucher_code, pos1, pos2):
        """
        Swap some string positions in the voucher code

        Parameters:
        ----------
        voucher_code : str
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

        voucher_code = self.swap(voucher_code, pos1, pos2)
        return voucher_code

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
        end = int(
            data[15]
        )  # Should be in the range of 2-4 (write a function to check, assert if not)

        amount_data = ""
        for i in range(0, end):
            pos = pow(2, i)
            amount_data += str(data[pos])
        amount = amount_data[::-1]  # reverse string
        return amount
