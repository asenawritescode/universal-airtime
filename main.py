from nanoid import generate as g

# Amounts from 10 - 1000  

def add_value(a , v):
    n = int(str(len(a)))
    i = n - 1
    for d in a:
        # Add the amount to the voucher
        pos = pow(2, i)
        v[pos] = d
        i-=1

    return ''.join(map(str, v))

def gen_voucher(amount):
   # check if amount is valid 
   if amount < 10 or amount > 1000:
        print("Invalid amount")
        return

   # Generate a random 12 digit number
   code = g("0123456789", 16 )
   # print(code, "code")
   # Convert to a list of integers
   v_str = list(str(code))
   a_str = list(str(amount))
   # Iterate
   v_digits = [int(digit) for digit in v_str]
   a_digits = [int(digit) for digit in a_str]

   final = add_value(a_digits, v_digits)
   print(final)
   return final