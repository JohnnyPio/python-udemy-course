# Function with Outputs
def format_name(f_name, l_name):
    #Docstring
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        print("Must have non-empty names.")
        return
    return f_name.title() + " " + l_name.title()

print(format_name("",""))


