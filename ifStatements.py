from traceback import print_exc

cars = ['audi', 'bmw', 'subaru', 'toyota']

# Checking for equality
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")

# Checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
else:
    print("No anchovies!")
print("\n")

# Using and to check multiple conditions
age_0 = 22
age_1 = 18
print("age_0 = " + str(age_0))
print("age_1 = " + str(age_1))
print("age_0 >= 21 and age_1 >= 21")
print(age_0 >= 21 and age_1 >= 21)
print("\n")

# Using or to check multiple conditions
age_0 = 22
age_1 = 18
print("age_0 = " + str(age_0))
print("age_1 = " + str(age_1))
print("age_0 >= 21 or age_1 >= 21")
print(age_0 >= 21 or age_1 >= 21)
print("\n")

# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(requested_toppings)
print("'mushrooms' in requested_toppings")
print('mushrooms' in requested_toppings)
print("\n")

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
print(banned_users)
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

print("\n")

# The if-elif-else chain
age = 12
print("Your age " + str(age))

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

print("\n")

# Omitting the else block
# Checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping)
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")