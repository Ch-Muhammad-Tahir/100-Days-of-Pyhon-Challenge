# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Get total Numbers Of items In a List
length_list = len(names)
random_number = random.randint(0, length_list-1)
print(f"{names[random_number]} is going to buy the meal today!")
print(random_number)
