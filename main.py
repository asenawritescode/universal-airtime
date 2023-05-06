from FeistelCipher import run

codes = ""
for _ in range(5): # Generate 5 vouchers 
    s = run()
    codes+= "{}\n\n".format(s)
# print(codes)

with open('file.txt', 'a') as file: # Open a file for appending
    file.write(codes) # Append a string to the file