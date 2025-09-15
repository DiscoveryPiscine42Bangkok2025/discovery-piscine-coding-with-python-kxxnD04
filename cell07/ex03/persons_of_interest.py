"""sort the dictionary by each element value"""
def famous_births(persons: dict):
    arr = sorted(persons.values(), key=lambda x: x["date_of_birth"])
    for person in arr:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
