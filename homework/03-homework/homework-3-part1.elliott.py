# Ben Elliott
# 2022-06-14
# Homework 3, Part 1


# PART ONE: Pokemon API

# Using the Pokemon API (Links to an external site.):

# What is the URL to the documentation? ✅
# What pokemon has the ID of 55? ✅
# How tall is that pokemon?  ✅
# How many versions of Pokemon games have been released?  ✅
# Print out the name of every electric-type pokemon. ✅
# What are electric-type Pokemon called in the Korean version of the game? ✅
# Who has a higher speed stat, Eevee or Pikachu?
# Tips

# Be sure to read the documentation!!!

# If a question cannot be answered using the API, answer it as "cannot be answered using the API."

# We kept seeing the word RESTful again and again. It's a pattern for APIs where you can make certain assumptions about how endpoints are set up. For example, when dealing with an endpoint that gives us ONE pokemon - for example, /pokemon/{id or name} - oftentimes just visiting /pokemon without an id will give us all of the pokemon.

# The language code for korean is ko

# When comparing Eevee and Pikachu, you'll need to make two requests to the API. Be careful you use different variable names each time, or you'll lose your data!

# You can't get the speed stat by looking at something['speed']. You'll need to use a loop, but only save the speed stat.


# What is the URL to the documentation?

print("The PokeAPI documentation can be found at:\nhttps://pokeapi.co/docs/v2\n")


# What pokemon has the ID of 55?

import requests

master_endpoint = "https://pokeapi.co/api/v2/"
response = requests.get(master_endpoint)
pokewiki = response.json()
# print(len(pokewiki))  # Okay, we have something.
# print(type(pokewiki))  # yay it's working!...
subpages = list(pokewiki.keys())  # a list of keys is often handy...
subpages_urls = list(pokewiki.values())  # so is a list of values...

pokeball = str(55)
# pokeball = input("What's the name or ID of the Pokémon you would like to dissect?")
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokeball}"

pokemon = requests.get(pokemon_url)
pokemon = pokemon.json()

print(
    f"{(pokemon['name']).capitalize()} has the ID {pokemon['id']} in the PokeAPI data structure."
)


# How tall is that pokemon?

print(
    f"{pokemon['name'].capitalize()} is listed as {pokemon['height'] / 10} meters tall in the PokeAPI data structure."  # listed in decimeters, which is weird. ==> meters
)


# How many versions of Pokemon games have been released?
# print(subpages)  # where might this info be
# print(type(subpages))  # what is it, again? it's a list.
# print(subpages.index('generation'))  # here looks good. it's index 14. there's our target url.
pokewiki_generation = str(subpages[14])

pokegeneration_url = f"https://pokeapi.co/api/v2/{pokewiki_generation}"
pokegen = requests.get(pokegeneration_url)
pokegen = pokegen.json()
# print(type(pokegen))  # good, it's a dict
# print(pokegen.keys())  # we want results! (PUN INTENDED)
# print(type(pokegen['results']))  # results is a list
# print(pokegen['results'])  # results is a list of dicts. Each with its own url.
# print(pokegen['results'][0]['url'])  # each gen has its own api url, wherein the information I need is buried. Joy of joys.

generation_urls = [generation["url"] for generation in pokegen["results"]]

version_groups = []  # assemble list of endpoint urls
for generation_endpoint in range(len(generation_urls)):
    target_url = (
        f"https://pokeapi.co/api/v2/generation/{str(generation_endpoint + 1)}/"
    )

    version_groups.append(target_url)

version_count = []  # init list of final count of game versions
generation_count = 0
for version in version_groups:
    generation = requests.get(
        version_groups[generation_count]
    )  # iter generations, dig version count, throw to list(version_count)
    generation = generation.json()
    version_count.append(len(generation["version_groups"]))
# print(version_count)

print(
    f"There have been {sum(version_count)} versions of Pokémon games across {generation_count} generations.\n"
)


# Print out the name of every electric-type pokemon.

types = requests.get("https://pokeapi.co/api/v2/type/")
types = types.json()
flavors = [
    types["results"][flavor_counter]["name"]
    for flavor_counter, flavor in enumerate(types["results"])
]

# print(flavors)

# flavors.index('electric')  # electric is index 12. pokemon counts from 1. electric is 'url/13'. Plus I have a handy list, now. I probably won't need it, but I have it. And that's not nothing.

electric = requests.get("https://pokeapi.co/api/v2/type/13")
electric = electric.json()
electric_pokemon = [
    electric["pokemon"][electric_counter]["pokemon"]["name"]
    for electric_counter, electremon in enumerate(electric["pokemon"])
]

# print(electric_pokemon)

print(
    f"Here's a list of all of the electric pokemon:\n\n{', '.join(str(zaprats.capitalize()) for zaprats in electric_pokemon)}.\n\nThere are {len(electric_pokemon)} of them.\n\nTo reduce your carbon footprint, you have to catch them all and wire them into your municipality's power grid.\n"
)


# What is the Korean word for electric-type Pokémon?

korean_counter = 0
korean_name = []
for language in electric["names"]:
    if electric["names"][korean_counter]["language"]["name"] == "ko":
        korean_name.append(electric["names"][1]["name"])
        break
    else:
        korean_counter += 1

# print(korean_name)

print(
    f"Electric-type Pokémon are called {korean_name[0]} in Korean.\n\nGoogle Translate says that this character is pronounced kind of like 'jeongi', which is super fun to say.\n"
)

# Who has a higher speed stat, Eevee or Pikachu?

pokeball = "pikachu"
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokeball}"

pokemon = requests.get(pokemon_url)
pokemon = pokemon.json()

# print(f"{(pokemon['name']).capitalize()} has the ID {pokemon['id']} in the PokeAPI data structure.")

# print(pokemon["name"])
pokemon["stats"]
pokemon["stats"][-1]  # here's our speed stat
pikaspeed = pokemon["stats"][-1]["base_stat"]


pokeball = "eevee"
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokeball}"

pokemon = requests.get(pokemon_url)
pokemon = pokemon.json()
pokemon["stats"]
pokemon["stats"][-1]  # here's our speed stat
evspeed = pokemon["stats"][-1]["base_stat"]
# print(evspeed)

print(f"Pikachu has a speed stat of {pikaspeed}")

print(f"\nEevee has a speed stat of {evspeed}")

print(f"\nPikachu is {pikaspeed - evspeed} speed-units faster than Eevee.")

print(f"\nIf my calculations are correct, then Pikachu is faster than Eevee.")
