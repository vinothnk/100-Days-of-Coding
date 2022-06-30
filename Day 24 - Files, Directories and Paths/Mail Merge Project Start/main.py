# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
placeholder = "[name]"

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines() # open as a list
    print(names)


with open('./Input/Letters/starting_letter.txt') as letters_file:
    letter = letters_file.read() # returns the content as a string

for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace(placeholder, stripped_name)
    print(new_letter)
    with(open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w')) as completed_letter:
        completed_letter.write(new_letter)






