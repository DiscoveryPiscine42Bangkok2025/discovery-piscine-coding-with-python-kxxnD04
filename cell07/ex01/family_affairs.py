"""filter family names that have red-hair"""
def find_the_redheads(family: dict) -> list:
    return list(filter(lambda name: family[name] == "red", family))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))
