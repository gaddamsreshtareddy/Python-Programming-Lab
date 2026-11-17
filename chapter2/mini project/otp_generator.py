# OTP Generator

import random

print("----- OTP GENERATOR -----")

otp = ""

for i in range(6):
    digit = random.randint(0, 9)
    otp = otp + str(digit)

print("Your OTP is:", otp)