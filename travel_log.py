# Personal Travel Logger
travel_log = [
    {
        "country": "India",
        "cities": ['Delhi', 'Punjab', 'Banaglore', 'Pune', 'Mumbai', 'Chennai'],
        "total_visit": 8
    },
    {
        "country": "France",
        "cities": ['Dijon', 'Lillies', 'Paros', 'Pune', 'Mumbai', 'Chennai'],
        "total_visit": 6
    }
]


def add_new_country(country, cities, total_visit):
    dict = {
        "country" : country,
        "cities": cities,
        "total_visit": total_visit
    }

    travel_log.append(dict)

add_new_country(country="Brazil",
                cities= ["Sao Paulo", "Rio de Janeiro"],
                total_visit=5)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['total_visit']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}")