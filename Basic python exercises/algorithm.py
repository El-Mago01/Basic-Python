#1. get the string
#2. identify the lenght of the string
#2a. If length >=4 return the string
#3. print # for length times
#4. identify the last 4 characters
#5. print the last 4 characters
#
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
#
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
#
# Examples (input --> output):
# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""
#
# // "What was the name of your first pet?"
# "Skippy" --> "##ippy"
# "Nananananananananananananananana Batman!" --> "####################################man!"


def maskify():
    string_to_mask=input("what string should be masked")
    if len(string_to_mask) <= 4:
        return string_to_mask
    masked_string+=string_to_mask[-4:]
    masked_string = "#" * len(string_to_mask)

    return masked_string

print(maskify())