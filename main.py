# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder: Tasneem Khan 
# Date: 16/2/26

# Write your code here
amt=float(input("Enter Principal Amount: "))
rate=float(input("Enter Rate of Interest: "))
time=float(input("Enter Time Period in Years: "))
si=amt*rate*time/100	#calculating simple interest

print(f"Simple Interest: {si}")
