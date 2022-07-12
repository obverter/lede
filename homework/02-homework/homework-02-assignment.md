HOMEWORK PART ZERO (totally 100% optional)
Fix the errors in 01-errors.py  Download 01-errors.py!

You should definitely work with other people on that one, it's fun to problem-solve. We won't be grading this one at all, but you should do it anyway, it's great practice.

A big issue is there are two kinds of errors in Python

Some happen when Python first reads the code, like if you forget to put a " or a ) - these are usually syntax errors. This is when Python is trying to understand what you want to do. If you didn't type it right, Python doesn't know what you mean!
Other errors happen when the Python code is running, called runtime errors. This is when Python is actually trying to do the things you tell it to do - like if you're trying to add a string and an integer and it gives you an error.
You'll need to fix all of type #1 before you can fix the type #2 errors. This means that you might need to fix syntax errors at the bottom of the page, then go back up to fix runtime errors once the code starts running!

Also, sometimes when you have an error, the error isn't actually on the line that it says the error is on (especially with syntax errors). Sometimes you need to look at a previous line of code to see the error!



HOMEWORK PART ONE
Please create a new file named homework-2-part1-lastname.py
The first line should be a comment with your full name
The second line should be the date
The third line should be a comment "Homework 2, Part 1"

PART ONE: Lists

Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
Display the number of elements in the list.
Display the 4th element of this list.
Display the sum of the 2nd and 4th element of the list.
Display the 2nd-largest value in the list.
Display the last element of the original unsorted list
Display the sum of all of the numbers divided by two.
Print whether the median or the mean of the numbers is higher
PART ONE: Dictionaries

1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)

5) Display the population of Brooklyn.

6) Display the combined population of all five boroughs.

7) Display what percent of NYC's population lives in Manhattan.

PART ONE: Tips

There are two ways to sort a list! One is just for display, and one sorts the list permanently. Keep an eye out for which one you're using.

Programmers are weird about counting. What number do they start with?

There might be a magic way to get the last item of a list in Python (or to start counting from the end).

When dealing with multiple numbers - population, for example - be sure to keep them all at the same level. If Brooklyn has 1.4 million people and Staten Island as 470,000, storing their population as 1.4 and 470000 isn't going to let you compare them accurately!

HOMEWORK PART TWO
Please create a new file named homework-2-part2-lastname.py
The first line should be a comment with your full name
The second line should be the date
The third line should be a comment "Homework 2, Part 2"

PART TWO: Lists

1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
2) Using a for loop, print each element of the list
3) Sort the list permanently.
4) Display the first element of the list.
5) Display the second-to-last element of the list.
6) Delete one of the countries from the list using its name.
7) Using a for loop, print each country's name in all caps.

PART TWO: Dictionaries

These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*, or use any other tool that exists online.

Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. (See here for explanation (Links to an external site.))

1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

PART TWO: Lists of dictionaries

1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).
2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
3) Loop through the list, printing whether each city is north of south of your tree from the previous section.

HOMEWORK PART THREE
Visit the following URL, then download the file by either clicking Download ZIP on the top right-hand corner or Raw on the right-hand side.

https://gist.github.com/jsoma/8cd1b74392975201705caf52f8fd0911 (Links to an external site.)

Download the file and save it as homework-2-part3-lastname.py
The first line should be a comment with your full name
The second line should be the date
The third line should be a comment "Homework 2, Part 3"


PART THREE: Applying your skills

It's more Spotify data, hooray! Explore it the same way we did in class - if you see a dictionary, examine its keys. Pick a key that might be useful, then go inside. If you see a list, take a look at the first element of the list. Keep going until you find what you're looking for.

Some parts of this one are VERY difficult, and some are easier. They aren't in order, so feel free to skip around! I also recommend going through the Little Columns tutorial a few times to make sure you're 100% on lists and dictionaries.

1. How many songs are there?

2. List the name of each song, along with its popularity.

3. How long would it take, in minutes, to listen to all of these songs in a row?

4. For each song, list every artist that worked on it.

5. For each song, list every musician that worked on it EXCEPT Drake

6. How many songs are from albums, and how many are from singles?

7. What percentage of these songs are marked as explicit?

8. I'd like to listen to one of the songs! Is there maybe a URL where I can listen to it?

9. What is the most popular song?

PART THREE: Tips

Is something a dictionary? Look at the keys! Is something a list? Look at the first one or use a for loop!

You'll probably want to use for loops, and continually add to a variable you're using for counting or totaling, like in http://littlecolumns.com/learn/python/counting-with-loops/. But you might need to be more specific than you think: let's say I'm telling a robot to count the number of brown eggs in my egg basket. Robots are dumb, so it's important that I tell it we're starting with 0 eggs.