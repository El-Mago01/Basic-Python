def sum_of_nums(numbers):
    sum = 0
    for num in numbers:
        sum +=  num
    return sum

numbers = [1,42,7]
print(sum_of_nums(numbers))