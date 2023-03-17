import os
import smtplib
import random as r
import math as m
otpsource = '0123456789abcdefghijklmnopqrstuvwxyz'
OTP=''
for i in range(6):
    OTP +=otpsource[m.floor(r.random()*otplen)]
otp= OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("mekalasowmya888@gmail.com", "1234567")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")