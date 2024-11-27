print("Hello Python World!")

message = "Hello World!"
print(message)
print("\n")

# Changing case in string with methods
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.lower())
print(name.upper())
print("\n")

# Combining or concatenating strings
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name )
print("\n")

# Adding whitespace to strings with tab or newlines
print("Python")
print("\tPython")
print("\nPython")
print("\n")

# Stripping whitespace
favorite_language = ' Python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

# Avoiding type errors with str() function
age = 23
message = "Happy" + str(age) + "rd Birthday"
print(message)