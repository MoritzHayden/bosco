# Convert an input string to screaming snake case
def to_screaming_snake_case(raw: str):
    return raw.strip().upper().replace(" ", "_")


# Convert an input string to title case
def to_title_case(raw: str):
    return raw.strip().replace("_", " ").title()
