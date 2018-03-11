# First time writing some code?
# Don't worry, I'll walk you through it.
#
# First, including a # in front of your code will turn it into a comment.

print("This gets printed into console")
# print("But this doesn't get printed")

# Now we need to create some variables.
# Create a variable called "name" and assign it your own name as a string.


# Create a variable called "age" and assign it your own age as an integer.


# Create a variable called "coolness" and give it a float.


# Create a variable called "likes_arnold" and give it a boolean.




# Now watch the magic happen.

if age > 130 or age < 1:
	raise IndexError("Your age is too high to be believable!")

cool_index = "Lame"

if likes_arnold == True:
	cool_index = "Very Lame"
elif coolness > 100.0:
	cool_index = "Cool Beans"
elif coolness > 75.0:
	cool_index = "Hella Rad",
elif coolness > 50.0:
	cool_index = "Pretty Nice"
elif coolness > 25.0:
	cool_index = "Kinda Sick"

padding = max(map(lambda x: len(str(x)) + 10, [name, cool_index]))

output = [
	"| Name: " + name,
	"| Age: " + str(age),
	"| Rating: " + str(cool_index)
]

print("-" * (padding + 2))
print(" |\n".join(map(lambda s: s.ljust(padding, " "), output)) + " |")
print("-" * (padding + 2))