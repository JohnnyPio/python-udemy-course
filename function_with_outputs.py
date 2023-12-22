# Function with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        print("Must have non-empty names.")
        return
    return f_name.title() + " " + l_name.title()

print(format_name("",""))
