"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""
colour1 = input("Warna pertama ? : ")
colour2 = input("Warna kedua ? : ")
adj = input("Rasa gula ? : ")
# Write a story with some words missing
# missing words are got from users inputs
story = """
Roses are {colour1}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""
# Ask the user to provide the missing words

# Display the final story
print(story.format(colour1=colour1,colour2=colour2,adjective=adj))