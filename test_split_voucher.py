"""Test cases for split_voucher.py"""
import unittest

import split_voucher


class TestSplitVoucher(unittest.TestCase):
    """Test cases for split_voucher.py"""

    def test_split_voucher(self):
        """Test split_voucher function"""
        self.assertEqual(split_voucher.split_voucher("123456"), ("123", "456"))
        self.assertEqual(split_voucher.split_voucher("023456"), ("023", "456"))
        self.assertEqual(split_voucher.split_voucher(123067), ("123", "067"))


if __name__ == "__main__":
    unittest.main()
