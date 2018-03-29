name = input("What is your name? ")
if (len(name)) > 20:
    print("Wow your name is long")
# If length of name is greater than 20,
# print something



age = input("What is your age?")
if int(age) < 10:
    print("Smol")
elif int(age) > 10 or age < 20:
    print("No show")
else:
    print("Big big boi")
# If age is less than 10, print "Smol"
# ELse if age is between 10 and 20, print "Big boi"
# Else, print "Big big boi"



coolness = input("Rate your coolness out of 100.0")
if float(coolness) > 100.0:
    print("error lie detected")
# If coolness is more than 100.0, just print some error


print("My name is Lee Zheng Jing, I am 17 and I'm not narcissistic enough to say im cool")
# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool
