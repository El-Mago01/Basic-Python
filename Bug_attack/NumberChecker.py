num = 0
def number_checker(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_checker(5)) # Expected output: Positive