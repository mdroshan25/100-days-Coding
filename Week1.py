print("This is my first program to develop")
print("Wish me good Luck")
print("I need to do fast to stay in country")

#print("enter your name")
name =input("enter your name")
age = int(input("enter your age:"))
phone = input("enter your phone no:")
print()
print("your name is:", name)
if age < 18:
    print(f"you are no major, cannont Vote as your age is:{age}")
else:
    print(f"you are elegible to vote as your age is:{age}")
if len(phone)<10:
    print(f"phone no provided is not correct,check again {phone}")
else:
    print(f"your phone no is:{phone}")

print("Your personal detailed entered, Thanks!!!")
