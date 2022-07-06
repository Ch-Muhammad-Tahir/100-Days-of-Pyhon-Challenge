# Conditional Statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is Your age? "))
    if age < 12:
        bill = 5
        print("Child's Tickets are $5 ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 25 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a good ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want photo taken? Y or N: ")
    if wants_photo == "Y" or wants_photo == "y":
        # Add $3 to their bill
        bill = bill + 3
    print(f"Your Final Bill is {bill}")


else:
    print("Sorry, you have to grow taller before you can ride.")
