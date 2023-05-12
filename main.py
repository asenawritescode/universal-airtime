"""Main module for the Universal-Aritime Project"""
from feistel_cipher import FeistelCipher
from invalid_voucher import InvalidVoucher
from retry_decorator import Retry

# Run the Feistel Cipher Algorithm


@Retry(tries=1000, delay=0, exceptions=(InvalidVoucher))
def main():
    """
    Runs the Feistel Cipher Algorithm
    """
    new_cipher = FeistelCipher(100, 1)
    # print(f.__dict__)
    voucher_code, plain_code, amount = new_cipher.cipher(
        new_cipher.cipher(new_cipher.voucher.code, new_cipher.flag), 0
    )
    output = f"Voucher Code -> {voucher_code} \nPlain Code -> {plain_code} \nAmount -> {amount}"
    return output


if __name__ == "__main__":
    CODES = ""
    for i in range(10):
        s = main()
        CODES += f"\n\n{s}"

    with open("50codes.txt", "a", encoding="utf-8") as fp:
        fp.write(CODES)
