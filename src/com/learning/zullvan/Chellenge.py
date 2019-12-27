story = """
In this story there are words missing, complete the words contained in the sign {}
Roses are {colours}
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
print('-'*100)

# Display the final story

print('Please fill in the missing words');
question = input('are you ready: ')
if question == 'y':
    print('-' * 100)
    colour = input('1. Roses are {colour} ? = ')
    colour2 = input('2. Violets are {colour2} ? = ')
    adjective = input('3. Sugar is {adjective} ? = ')
    me = input('And so are you ?= ')
elif question == 't':
    print('-' * 100)
    print('Terima Kasih')
    exit()

print('----------------------------------------------Result------------------------------------------------')
print(f"Roses are {colour}")
print(f"Violets are {colour2}")
print(f"Sugar is {adjective}")
print(f"And so are you {me}")
print('-----------------------------------------------End--------------------------------------------------')
