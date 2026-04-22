# Exercises based upon the master class of Lean
# See also: https://app.masterschool.com/campus/notion/67b064bc849b47e8975f45a83a8afe91

fruits=['apple', 'banana', 'grape']
vegetables=['carrot', 'broccoli', 'spinach']
produce=fruits+vegetables
print(produce[0:3])

animals = ['tiger', 'lion', 'elephant', 'goat', 'dog', 'whale']
animals.append('snake')
animals.insert(0,'monkey')
animals.pop(-1)
animals.remove('lion')
animals.insert(1,"cat")
print(animals)

animals=['tiger', 'lion', 'elephant', 'goat', 'dog',  'whale']

to_add=input("what animal shall be added to the zoo: ")
to_remove=input("what animal shall be removed from the zoo:")
animals.insert(0,to_add)
try:
    animals.remove(to_remove)
except Exception as e:
    print(f"Not possible to remove {to_remove}")

print (animals)

scores=[30, 50, 90, 46, 50, 72, 20]
print(sum(scores))
print(len(scores))
print(sum(scores)/len(scores))
print(scores.count(50))
print(max(scores))
print(min(scores))
