def calc_tax(income):
    return 0.037*income

def multiply_floats(num1, num2):
    return num1*num2


name=input("What's your name ")
#income=float(input("What's your montly income "))

#tax_to_be_paid=calc_tax(income)
#print(f"Hello Name, your current tax due is {round(tax_to_be_paid,2)} with the amount rounded down")

num1=float(input("Nr 1: "))
num2=float(input("Nr 2: "))
print(f"Hi Name, {name} {num1} multiplied by {num2} equals {multiply_floats(num1,num2)}")