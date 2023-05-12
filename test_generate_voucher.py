"""Test cases for generate_voucher.py"""
import unittest

import generate_voucher


class TestVoucher(unittest.TestCase):
    """Test cases for generate_voucher.py"""

    def test_amount(self):
        """Test amount attribute"""
        voucher_1 = generate_voucher.Voucher(100)
        voucher_2 = generate_voucher.Voucher(200)

        self.assertEqual(voucher_1.amount, 100)
        self.assertEqual(voucher_2.amount, 200)

    def test_code(self):
        """Test code attribute"""
        voucher_1 = generate_voucher.Voucher(100)
        voucher_2 = generate_voucher.Voucher(200)

        self.assertEqual(len(voucher_1.code), 16)
        self.assertEqual(len(voucher_2.code), 16)

    def test_add_value(self):
        """Test add_value method"""
        voucher_1 = generate_voucher.Voucher(10)

        data = list("1234567891234567")
        data_list = [int(digit) for digit in data]
        amount = list("294")
        amount_list = [int(digit) for digit in amount]
        voucher_1.code = data_list

        self.assertEqual(
            voucher_1.add_value(voucher_1.code, amount_list), "1494267891234563"
        )

    def test_gen_voucher(self):
        """Test gen_voucher method"""

        self.assertRaises(ValueError, generate_voucher.Voucher, 9)
        self.assertRaises(ValueError, generate_voucher.Voucher, 1001)


if __name__ == "__main__":
    unittest.main()
