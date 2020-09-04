# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
# temp.name[0] checks the first letter
a = [t.name for t in humans if t.name[0] is "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# The -1 will drop us to the last element in the array
b = [t.name for t in humans if t.name[-1] is "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# This one was a bit more tricky, had to look up python methods that allowed you to take a range and the order method
c = [t.name for t in humans if ord(t.name[0]) in range(ord("C"), ord("H"))]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# Setting the list comprehension with a +10 allows to set range without adding an additional conditional
d = [t.age + 10 for t in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# Used a f string to set it up
e = [f"{t.name}-{t.age}" for t in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(t.name, t.age) for t in humans if t.age in range(27, 33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(t.name.upper(), t.age + 5) for t in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(t.age) for t in humans]
print(h)
