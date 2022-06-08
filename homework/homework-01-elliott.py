# Ben Elliott
# 2022-06-07
# Homework 1

# When run from the command line, this file should prompt the user for their year of birth, and print out (approximately):

import numpy as np # Sorry about the numpy import. I'm using it exactly once for a funner heart rate calculation.

print(
    "\n ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ \n ♡♡♡♡♡♡♡♡♡♡♡♡ Welcome to the Life Comparifier ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ \n ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡ \n"
)

# How old the user is
# If someone says they were born in the future, try asking them again (assume they'll do it right the second time).

while True:
    age = int(input("How old are you? \n > "))
    try:
        age > 0
        break
    except ValueError:
        print("You are not a time traveler. Please enter your actual age.")

# constants
DAYS = age * 365.25
HOURS = age * 365 * 24
MINUTES = age * 365 * 24 * 60
VENUS = round(age * 1.615, 2)
NEPTUNE = round(age / 165, 2)

pulse = np.random.normal(65.9, 9.7)
total_beats = round(pulse * MINUTES)
whale = round(total_beats / pulse * 11)  # Blue Whale RHR ~11
rabbit = round(total_beats / pulse * 135)  # Rabbit RHR ~120-150
birthyear = 2022 - age


# How many times the user's heart has beaten
print(
    "\nAccording an enormous NIH study, the average adult's resting heart rate \nis about 66 beats per minute (MEAN: 65.9, STD DEV: 9.7).\n "
)
print(
    "So let's generate a random value from a normal distribution of \nthe NIH's resting heart rate study and say that it's \nyour resting heart rate... \n"
)
print("It is done. \n")

print(
    "Guido van Rossum, who is Python's creator and, \nprior to his resignation, was Python's \nBenevolent Dictator for Life, has wiggled his fingers and \ndetermined that your resting heart rate is...\n"
)

print("❤️ ❤️ ❤️ ", round(pulse), "beats per minute. ❤️ ❤️ ❤️\n ")
print(
    "If you don't like your resting heart rate, don't blame Guido.\n\nMaybe do some cardio.\n"
)

print("But now that Guido has given you a heart rate, here are some mostly-fun facts:\n")
print(
    "Your heart has beaten about",
    round(total_beats / 1_000_000_000, 3),
    "billion times during your lifetime. \n",
)

# How many times a blue whale's heart has beaten
print(
    "If Guido turned you into a blue whale that was",
    age,
    "years old, \n then your heart would have beaten about",
    round(whale / 1_000_000),
    "million times. 🐳 🐳 🐳 \n",
)

# How many times a rabbit's heart has beaten
# If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number
print(
    "But if Guido made you a rabbit that was",
    age,
    "years old, \n then your heart would have beaten about",
    round(rabbit / 1_000_000_000, 3),
    "billion times. 🐰 🐰 🐰 \n",
)

# How old they are in Venus years
print(
    "If you had been born on Venus, \n you would have been incinerated \n",
    VENUS,
    "Venitian years ago. \n 🔥 🔥 🔥\n 🔥 HOT 🔥\n 🔥 🔥 🔥\n",
)

# How old they are in Neptune years
print(
    "But if you had been born on Neptune, \n you would have been crushed and frozen \n",
    NEPTUNE,
    "Neptunian years ago. \n \n ☃️ ☃️ ☃️  ¡Cool! ☃️ ☃️ ☃️\n \n",
)

# Whether they are the same age as you, older or younger
#  If older or younger, how many years difference
if age > 37:
    print(
        "And since you're",
        age,
        ", you'll always be",
        round(abs(age - 37)),
        "years older \n than the person who wrote this code. 💀 💀 💀 \n",
    )
elif age < 37:
    print(
        "And since you're",
        age,
        ", you'll always be",
        round(abs(age - 37)),
        "years younger \n than the person who wrote this code. 👶 👶 👶\n",
    )
else:
    print("Oh hey! The person who wrote this code is 37 too!\n")

# If they were born in an even or odd year

if birthyear % 2 == 0:
    print("You were born in", birthyear, "which is an even year.\n")
else:
    print(
        "You were born in",
        birthyear,
        "which is an odd year.\nOdd-numbered. Most years are pretty odd.\n",
    )

# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)

democrats = [1960, 1963, 1976, 1992, 2008, 2020]

print(
    "There have been",
    sum(i <= birthyear for i in democrats),
    "Democratic presidents in office since you showed up.\n",
)


# Which US President was in office when they were born (1960 onward)

presidents = {
    range(1953, 1960): "Eisenhower",
    range(1961, 1963): "Kennedy",
    range(1964, 1968): "Johnson",
    range(1969, 1974): "Nixon",
    range(1975, 1976): "Ford",
    range(1977, 1980): "Carter",
    range(1981, 1988): "Reagan",
    range(1989, 1992): "Bush",
    range(1993, 2000): "Clinton",
    range(2001, 2008): "Dubya",
    range(2009, 2016): "Obama",
    range(2017, 2020): "Trump",
    range(2021, 2022): "Biden",
}

in_office = {presidents[key] for key in presidents if birthyear in key}

print(f"{in_office} was probably the President when you were born")
