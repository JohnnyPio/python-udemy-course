#TODO: Create a letter using starting_letter.txt
all_names = []
with open("Input/Names/invited_names.txt", "r") as names_file:
    raw_read = names_file.readlines()
    for names in raw_read:
        all_names.append(names[:-1])


#for each name in invited_names.txt
with open("Input/Letters/starting_letter.txt", "r") as letter:
    contents = letter.read()
    for name in all_names:
        new_letter = contents.replace("[name]", f"{name}")
        new_file = open(f"Output/ReadyToSend/letter for {name}.txt", "w")
        new_file.write(new_letter)
        new_file.close()

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp