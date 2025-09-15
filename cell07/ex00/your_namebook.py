"""display lists of full names from dictionary"""

def array_of_names(persons: dict):
    names = []
    for first, last in persons.items():
        names.append(f"{first.capitalize()} {last.capitalize()}")
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))
