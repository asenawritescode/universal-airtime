from RetryDecorator import Retry
from InvalidVoucher import InvalidVoucher
from FeistelCipher import FeistelCipher
# Run the Feistel Cipher Algorithm

@Retry(tries=1000, delay=0, exceptions=(InvalidVoucher))
def run():
    """
    Runs the Feistel Cipher Algorithm
    """
    f = FeistelCipher(198, 1)
    # print(f.__dict__)
    e, p, a = f.cipher(f.cipher(f.voucher.code, f.flag), 0)
    output = f'Voucher Code -> {e} \nPlain Code -> {p} \nAmount -> {a}'
    return output
        
codes = ""        
for i in range(10):
    s = run()
    codes += "{}\n\n".format(s)

with open("codes.txt", "a") as f:
    f.write(codes)