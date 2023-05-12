"""Test cases for feistel_cipher module."""
import unittest

import feistel_cipher
from invalid_voucher import InvalidVoucher


class TestFeistelCipher(unittest.TestCase):
    """Test cases for the feistel_cipher module."""

    def test_exceptions_cipher(self):
        """Test exceptions in cipher method."""
        f_test = feistel_cipher.FeistelCipher(100, 2)

        self.assertRaises(
            InvalidVoucher, f_test.cipher, "12345678912345678", 0
        )  # check for length gt 16
        self.assertRaises(
            InvalidVoucher, f_test.cipher, "123456789123456", 0
        )  # check for odd numbers
        self.assertRaises(UserWarning, f_test.cipher, "1234567891234567", 3)

    def test_cipher(self):
        """Test cipher method."""
        f_test = feistel_cipher.FeistelCipher(100, 2)

        self.assertEqual(
            f_test.cipher("5503110350118885", 0),
            ("5503110350118885", "6003110500129983", "100"),
        )
        self.assertEqual(f_test.cipher("5001121134828643", 1), "5601121764839452")


if __name__ == "__main__":
    unittest.main()
