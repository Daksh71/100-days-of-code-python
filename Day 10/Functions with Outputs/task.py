def format_name(firstname,lastname):
    return firstname.title(),lastname.title()

print(format_name("DAKSH","MITTAL"))


def format_name(firstname, lastname):
    full_name = f"{firstname.title()} {lastname.title()}"
    return full_name

result = format_name("DAKSH", "MITTAL")
print(result)