"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""
# Write a story with some words missing
# missing words are got from users inputs
story = """
In this story there are words missing, complete the words contained in the sign {} \n
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""
def colour(x):
    return x
def colour2(x):
    return x
def adjective(x):
    return x
def me(x):
    return x
# Ask the user to provide the missing words
print(story)

# Display the final story

print(' \033[91m Please fill in the missing words \033[0m');
colour = input('1. Roses are {colour} ? = ')
colour2 = input('2. Violets are {colour2} ? = ')
adjective = input('3. Sugar is {adjective} ? = ')
me = input('And so are you ?= ')

print('-'*100)
print(f"Roses are {colour}")
print(f"Violets are {colour2}")
print(f"Sugar is {adjective}")
print(f"And so are you {me}")
