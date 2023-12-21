programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
#Retrieve items
# print(programming_dictionary["Function"])

#Add new items
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#Create an existing dictionary
empty_dictionary = {}

# #Wipe an existing dict.
# programming_dictionary = {} 
# print(programming_dictionary)

#Edit an item in a dict.
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dict.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    