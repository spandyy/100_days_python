travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]



def add_new(country, visits, cities):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["cities"]=cities

    travel_log.append(new_country)

    print(travel_log)


add_new("Russia", 2, ["Moscow", "Saint Petersburg"])