# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:Tasneem Khan
# Date:02-03-2026

# Write your code here
print("---Simple Interest Calculator---")
#To take principal from the user
principal=float(input("Enter the principal:"))
#To take interest from the user
intrst=float(input("Enter the rate of interest:"))
#TO take time period from the user
time=float(input("Enter the time period(in years):"))
#formula of simple interest
SI=(principal*intrst*time)/100
print("Simple interst =",SI)                                        
