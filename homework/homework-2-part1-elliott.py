# PART ONE: Lists

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]
print(f"Here is a list of numbers:\n✪ ✪ ✪ {numbers} ✪ ✪ ✪\n")

# Display the number of elements in the list.
print(f"There are {len(numbers)} numbers in the list.\n")

# Display the 4th element of this list.
print(f"{numbers[3]} is the fourth element of this list\n")

# Display the sum of the 2nd and 4th element of the list.
print(
    f"The sum of the second and fourth element of the list is {numbers[1] + numbers[3]}\n"
)

# Display the 2nd-largest value in the list.
sorted = sorted(numbers)
print(f"The second-largest value in the list is {sorted[-2]}\n")

# Display the last element of the original unsorted list
print(f"The last element of the original unsorted list is {numbers[-1]}\n")

# Display the sum of all of the numbers divided by two.
print(f"The sum of all of the numbers divided by two is {sum(numbers) / 2}\n")

# Print whether the median or the mean of the numbers is higher
def median(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[~mid]) / 2


def mean(data):
    return sum(data) / len(data)


if median(numbers) > mean(numbers):
    print(
        f"The median of the list is larger than the mean. ({median(numbers)} > {mean(numbers)}\n"
    )
else:
    print(
        f"The mean of the list is larger than the median. ({int(mean(numbers))} > {int(median(numbers))})\n\n"
    )
print("✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪\n\n")
# PART ONE: Dictionaries

# 1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {
    "title": "Gigli",
    "year": 2003,
    "director": "Martin Brest",
    "budget": 76_000_000,
    "revenue": 7_200_000,
}

print(
    f"My favorite movie is {movie['title']}, which was released in {movie['year']} and was directed by {movie['director']}.\n"
)

# 2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
# 3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

delta = movie["budget"] - movie["revenue"]
K = 1000
M = 1_000_000

if delta > 0:
    print(
        f"{movie['title']} lost {(delta / M)} million dollars, which made it a terrible investment, and {movie['director']} never worked in Hollywood again.\n"
    )
elif delta > (movie["budget"] * 5):
    print(
        f"{movie['title']} made {abs(delta / M),.1} million dollars in profit, and that was a great investment.\n"
    )
else:
    print(
        f"{movie['title']} made {abs(delta / M),.1} million dollars in profit, and that was a good investment.\n"
    )

# 4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)

# NYC population in millions.
nyc = {
    "Manhattan": 1.6,
    "Brooklyn": 2.6,
    "Bronx": 1.4,
    "Queens": 2.3,
    "Staten Island": 0.47,
}

# 5) Display the population of Brooklyn.
print(f"Brooklyn has a population of {nyc['Brooklyn']} million people.\n")

# 6) Display the combined population of all five boroughs.
nyc_sum = sum(nyc.values())
print(f"New York City has a population of {nyc_sum} million people.\n")

# 7) Display what percent of NYC's population lives in Manhattan.
print(
    f"Approximately {(nyc['Manhattan'] / nyc_sum * 100):0.2f}% of New Yorkers live in Manhattan."
)

# PART ONE: Tips

# There are two ways to sort a list! One is just for display, and one sorts the list permanently. Keep an eye out for which one you're using.

# Programmers are weird about counting. What number do they start with?

# There might be a magic way to get the last item of a list in Python (or to start counting from the end).

# When dealing with multiple numbers - population, for example - be sure to keep them all at the same level. If Brooklyn has 1.4 million people and Staten Island as 470,000, storing their population as 1.4 and 470000 isn't going to let you compare them accurately!
