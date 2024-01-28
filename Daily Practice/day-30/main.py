# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = ("key","value")
# value = a_dictionary["fake_key"]
#
# IndexError
# fruit_list = ["Apple", "Banana"]
# fruit = fruit_list[4]
#
# TypeError
# text = 'abc'
# print(text+5)

# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} doesn't exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
