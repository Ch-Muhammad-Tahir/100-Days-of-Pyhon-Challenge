# Randomization
import random

random_interger = random.randint(1, 10)
# print(random_interger)

random_float = random.random()  # Generate  Random value Between 0 and 1 (0.0000000.. to 0.999999.....)
# print(random_float)

# print(random_float * 5)

# -------------------------------------------------Lists---------------------------------------------
# Lists are used to store multiple items in a single variable.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])

print(states_of_america[-1]) # Staring From End of The List
print(states_of_america[-2])

# Edit Item Of a List
states_of_america[1] = "London"
print(states_of_america[1])

# Add Item In end Of a List

states_of_america.append("Canada")
print(states_of_america)

# Adding a bunch of item list In a list
states_of_america.extend(["New State1", "New State2", "New State2"])
print(states_of_america)



