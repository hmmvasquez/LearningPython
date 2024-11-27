bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print('\n')

# Accessing elements in a list
# Index positions start at 0, Not 1
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print('\n')

# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print('\n')
motorcycles[0] = 'ducati'
print(motorcycles)
print('\n')

# Appending elements to the end of a list
motorcycles.append('honda')
print(motorcycles)
print('\n')

# Inserting elements into a list
motorcycles.insert(2, 'brand')
print(motorcycles)
print('\n')

# Removing an item using del statement
del motorcycles[2]
print(motorcycles)
print('\n')

# Removing an item using the pop() method
# Extract the last item of a list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print('\n')

# Popping items from any position in a list
second_owned = motorcycles.pop(1)
print(second_owned)
print('\n')

# Removing an item by value
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print('\n')

# Sorting a list permanently with the sort method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.sort()
print(motorcycles)
print('\n')

# Sorting a list temporarily with the sorted() function
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
print(sorted(motorcycles))
print(motorcycles)
print('\n')

# Printing a list in reverse order
print(motorcycles)
motorcycles.reverse()
print(motorcycles)
print('\n')

# Finding the length of a list
print(motorcycles)
print(len(motorcycles))

# Looping through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# Making numerical list
# Using the range() function
for value in range(1,5):
    print(value)

# Using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

# Even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(digits)
print("Min: " + str(min(digits)))
print("Max: " + str(max(digits)))
print("Sum: " + str(sum(digits)))

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorites foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friends_foods)