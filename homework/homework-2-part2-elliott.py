# Ben Elliott
# 2022-06-07
# Homework 2, Part 2

# PART TWO: Lists

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = ["Canada", "Paraguay", "Chad", "Mexico", "China", "Japan", "Spain"]
# 2) Using a for loop, print each element of the list
print("Here is a list of countries.\n")
for i in countries:
    print(i)

# 3) Sort the list permanently.
countries_abc = sorted(countries)

print(f"\nLet's alphabetize the list permanently:\n\n{countries_abc}\n")

# 4) Display the first element of the list.
print(f"The first entry in the alphabetized list of countries is {countries_abc[0]}.\n")

# 5) Display the second-to-last element of the list.
print(
    f"The second-to-last entry in the alphabetized list of countries is {countries_abc[-2]}.\n"
)

# 6) Delete one of the countries from the list using its name.

print("And then, for all the obvious reasons, let's get rid of Canada:\n")

countries_abc.remove("Canada")
print(countries_abc)

# 7) Using a for loop, print each country's name in all caps.

print(
    "\nFinally, let's celebrate the non-Canadian list members by shouting their names:\n"
)

for i in range(len(countries_abc)):
    countries_abc[i] = countries_abc[i].upper()

print(countries_abc)

print("\n🇨🇦 🇨🇦 🇨🇦 🇨🇦 🇨🇦 🇨🇦 🇨🇦 🇨🇦 🇨🇦 🇨🇦\n")

# PART TWO: Dictionaries

# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*, or use any other tool that exists online.

# Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. (See here for explanation (Links to an external site.))

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
print(
    "Let's create a dictionary called 'tree' that responds to a set of tree-related keys:\n"
)
tree = {}
key_list = ["name", "species", "age", "location_name", "latitude", "longitude"]
tree_values = [
    "Hyperion",
    "coast redwood",
    "750",
    "Redwood National Park",
    "41.3",
    "-124",
]
for i in key_list:
    tree[i] = None

print(tree)

print(
    "\nThat's boring. Let's cram the world's largest tree into this empty dictionary:\n"
)

tree = {}
for key in key_list:
    for value in tree_values:
        tree[key] = value
        tree_values.remove(value)
        break

print(str(tree))


# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

print(
    f"{tree['name']} is a {tree['age']}-year-old tree that is in {tree['location_name']}.\n"
)

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

nyc = {"latitude": "40.7128", "longitude": "-74.0059"}

if tree["latitude"] < nyc["latitude"]:
    print(f"{tree['name']} in {tree['location_name']} is south of NYC.\n")
else:
    print(f"{tree['name']} in {tree['location_name']} is north of NYC.\n")

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
age = input("How old are you?\n >")

print("Okay, let me crunch the numbers...")
import time

time.sleep(1)

for i in range(3):
    time.sleep(i)
    print("\nCALCULATING...")


if int(age) > int(tree["age"]):
    time.sleep(1)
    print(
        f"Get a load of this! You're {int(age) - int(tree['age'])} years older than {tree['name']}"
    )
else:
    time.sleep(1)
    print(
        f"\nYou're never going to believe this, but you're {abs(int(age) - int(tree['age']))} years younger than {tree['name']}"
    )

# PART TWO: Lists of dictionaries

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).
# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
print("\n\n🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺\n")
places = {  # grab info from wikipedia
    "moscow": "55.7558° N, 37.6173° E",
    "tehran": "35.7219° N, 51.3347° E",
    "falkland_islands": "51.7963° S, 59.5236° W",
    "seoul": "37.5665° N, 126.9780° E",
    "santiago": "33.4489° S, 70.6693° W",
}

coordinates = []  # init working lists
lats = []
longs = []

for pair in places.values():  # iter places.values, split, throw to working lists.
    pair = pair.split(",")
    for coords in pair:
        if "N" in coords or "S" in coords:  # parse lats, else longs
            lat = coords
            lat = lat.strip()  # kill any whitespace
            if "S" in lat:
                lat = lat[0:-3]  # kill NS token
                lat = float(lat)
                lat = lat * -1  # neg subset for S
                lats.append(lat)
            else:
                lat = lat[0:-3]
                lat = float(lat)
                lats.append(lat)
        else:  # repeat NS block for EW
            long = coords
            long = long.strip()
            if "W" in long:
                long = long[0:-3]
                long = float(long)
                long = long * -1
                longs.append(long)
            else:
                long = long[0:-3]
                long = float(long)
                longs.append(long)

cities = []
city_counter = 0
for city in places:  # init dictionary per homework problem
    city = {"name": city, "lat": lats[city_counter], "long": longs[city_counter]}
    city_counter += 1
    cities.append(city)

for destination in cities:
    dname = destination["name"]
    if "falkland" not in dname:  # sequester falkland
        if destination["lat"] > 0:
            print(f"{str(dname).capitalize()} is north of the equator.\n")
        else:
            print(f"{str(dname).capitalize()} is south of the equator.\n")
    else:
        if destination["lat"] > 0:
            print(f"{str(dname).capitalize()} is north of the equator.")
        else:
            print(f"{str(dname).capitalize()} is south of the equator.")
        print(
            "The Falkland Islands are a biogeographical part of the mild Antarctic zone.\n"
        )

print("🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺🌲🗺\n")  # obligate emoji

for destination in cities:
    dname = destination["name"]
    if destination["lat"] > float(tree["latitude"]):
        print(f"{str(dname).capitalize()} is north of {tree['name']}.\n")
    else:
        print(f"{str(dname).capitalize()} is south of {tree['name']}.\n")
