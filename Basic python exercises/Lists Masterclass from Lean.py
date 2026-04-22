# Sacks of Gold
# I’ve just robbed a bank 🏦. Here is a list of the weight of the sacks of gold I stole. How much do they weigh in total?
from django.db.models import Avg

sacks = [2.33, 4.1, 8.5, 6.66, 2.4]

print(f"The total weight of the sacks is: {sum(sacks)}")

weight=0
for sack in sacks:
    if sack<5:
        weight+=sack

print(f"The weight of the sacks that are less than 5 kg is : {weight}")

#
# I hope it’s a lot… 🤑💰
# The Escape
# Oh no! the police is here! I need to get rid of some weight to run fast. How much will the sacks weigh if
# I throw away the ones that are heavier than 5kg? 😨
# Bad Luck
# I have many pearl necklaces. However some of them bring bad luck. How many necklaces have 13 pearls in them? 🦪


# Bad Luck
# I have many pearl necklaces. However some of them bring bad luck. How many necklaces have 13 pearls in them? 🦪
necklaces = [12, 13, 22, 18, 13, 10, 30, 15, 13, 12]
print(f"The number of necklesses with 13 pearls : {necklaces.count(13)}")

# Common Names
# Here is a list of common names. 👨🏽‍🦱👩🏽
# How many of them start with “H”?
# How many of them start with “L” and are 4 letters long?

names = ["Emma", "Felix", "Henry", "Linn", "Lina", "Felix", "Hannah", "Noah", "Marie", "Leon"]

start_with_H=0
start_with_L_and_len4=0
for name in names:
    if name[0] == 'H':
        start_with_H +=1
    if name[0] == 'L' and len(name) == 4:
        start_with_L_and_len4+=1

print(f"number of names starting with H                          : {start_with_H}")
print(f"number of names starting with L and longer than 4 letters: {start_with_L_and_len4}")

# Warehouse
# In the warehouse I have 8 big boxes, each one of them contains 4 medium sized boxes, each containing 6 small boxes.
# How many boxes do I have? 🏭

boxes = [8, 4, 6]
nr_of_boxes=boxes[0]*boxes[1]*boxes[2]
print(f"The number of boxes in the warehouse is: {nr_of_boxes}")


# Bonus: Class Average
# I’ve finally finished grading all of my students tests. I wonder, what is the class average? 📑

grades = [1.0, 2.1, 1.5, 3.0, 1.0, 1.2, 3.5, 1.0]
print(f"The average of the class: {sum(grades)/len(grades)}")


# Bonus: 5km Run
# I go out running 5 km every day and record my time. What was my fastest run? 🏃🏽‍➡️

times = [31.3, 29.8, 29.4, 30.3, 28.9, 29.4]
print(f"The fastest run was : {min(times)}")


