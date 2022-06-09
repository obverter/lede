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

countries_abc.remove('Canada')
print(countries_abc)

# 7) Using a for loop, print each country's name in all caps.

print("\nFinally, let's celebrate the non-Canadian list members by shouting their names:\n")

for i in range(len(countries_abc)):
    countries_abc[i] = countries_abc[i].upper()

print(countries_abc)

# PART TWO: Dictionaries

# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*, or use any other tool that exists online.

# Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. (See here for explanation (Links to an external site.))

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

# PART TWO: Lists of dictionaries

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).
# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
