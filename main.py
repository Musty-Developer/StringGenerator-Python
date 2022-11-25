import random

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
SYMBOLS = "`!@#$%^&*()_+{}\"';:\|<>?/"
NUMBERS = "1234567890
LENGTH = input("Password Length: ")

COMBINED = UPPER_CASE + LOWER_CASE + SYMBOLS + NUMBERS 

OUTPUT = "".join(random.sample(COMBINED, LENGTH))
print(OUTPUT)
