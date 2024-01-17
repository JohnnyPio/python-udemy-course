all_names = []
with open("Input/Names/invited_names.txt", "r") as names_file:
    raw_read = names_file.readlines()
    for names in raw_read:
        all_names.append(names.strip())


with open("Input/Letters/starting_letter.txt", "r") as letter:
    contents = letter.read()
    for name in all_names:
        new_letter = contents.replace("[name]", f"{name}")
        new_file = open(f"Output/ReadyToSend/letter for {name}.txt", "w")
        new_file.write(new_letter)
        new_file.close()
