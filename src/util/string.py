# Convert an input string to screaming snake case
def to_screaming_snake_case(input: str):
    return input.strip().upper().replace(" ", "_")


# Convert an input string to title case
def to_title_case(input: str):
    return input.strip().replace("_", " ").title()
