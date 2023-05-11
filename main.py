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
    f = FeistelCipher(50, 1)
    # print(f.__dict__)
    e, p, a = f.cipher(f.cipher(f.voucher.code, f.flag), 0)
    output = f"Voucher Code -> {e} \nPlain Code -> {p} \nAmount -> {a}"
    return output


if __name__ == "__main__":
    codes = ""
    for i in range(2000):
        s = main()
        codes += "{}\n\n".format(s)

    with open("50codes.txt", "a") as f:
        f.write(codes)
