# Register for an account at weatherapi.com.

# What is the URL to the documentation?
# Make a request for the current weather where you are born, or somewhere you've lived.
# Print out the country this location is in.
# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
# What URL would I use to request a 3-day forecast at Heathrow?
# Print the date of each of the 3 days you're getting a forecast for.
# Print the maximum temperature of each of the days.
# Print the day with the highest maximum temperature.
# TIPS

# Be sure to read the documentation!!!

# If a question cannot be answered using the API, answer it as "cannot be answered using the API."

# Make sure you've registered for an API key! It goes in the URL like this - http://api.weatherapi.com/v1/current.json?key=c52fbcfa1fa84d819e114406200211&q=London - note that instead of being part of the URL, your variables are URL parameters.

# Be careful when cutting and paste your API key, it's easy to accidentally also copy and paste "LIVE"

# Take advantage of the API Explorer - https://www.weatherapi.com/api-explorer.aspx (Links to an external site.) - it will build requests for you with simple dropdowns. Don't forget to paste in your API key!

# For the airport code, you'll need to read the documentation for forecasts as well as Google for the airport code.

# To get the "day with the highest maximum temperature," you might pay attention to the end of me doing the Spotify homework. I sped through it, but the code isn't too different!


print("What is the URL to the documentation?\n")
print("https://www.weatherapi.com/docs/\n")
print("\n- - - - - - - - - - - - - - - - - - -\n")


import requests


print(
    "Make a request for the current weather where you are born, or somewhere you've lived.\n"
)
key = "6e398a633db74946801165709221306"
loc = "Stockton"
query_url = "http://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + loc
stockton = requests.get(query_url)
stockton = stockton.json()
# print(stockton)
print(
    f"The current temperature in {stockton['location']['name']}, {stockton['location']['region']} is {stockton['current']['temp_f']}°F"
)
print("\n- - - - - - - - - - - - - - - - - - -\n")

# Print out the country this location is in.
print(
    f"{stockton['location']['name']}, {stockton['location']['region']} is located in the {stockton['location']['country']}."
)
print("\n- - - - - - - - - - - - - - - - - - -\n")

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.

if stockton["current"]["temp_f"] > stockton["current"]["feelslike_f"]:
    print(
        f"The current temperature in {stockton['location']['name']}, {stockton['location']['region']} is {stockton['current']['temp_f']}°F, but it feels {abs(stockton['current']['temp_f'] - stockton['current']['feelslike_f'])}°F cooler."
    )
elif stockton["current"]["temp_f"] < stockton["current"]["feelslike_f"]:
    print(
        f"The current temperature in {stockton['location']['name']}, {stockton['location']['region']} is {stockton['current']['temp_f']}°F, but it feels {abs(stockton['current']['temp_f'] - stockton['current']['feelslike_f'])}°F warmer."
    )
elif stockton["current"]["temp_f"] == stockton["current"]["feelslike_f"]:
    print(
        f"The current temperature in {stockton['location']['name']}, {stockton['location']['region']} is {stockton['current']['temp_f']}°F, and that's exactly the temperature it feels."
    )

print("\n- - - - - - - - - - - - - - - - - - -\n")
print(
    "\nWhat's the current temperature at Heathrow International Airport?\n"
)  # Use the airport's IATA code to search."
loc = "LHR"
query_url = "http://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + loc
location = requests.get(query_url)
location = location.json()
# print(stockton)
print(
    f"The current temperature in {stockton['location']['name']}, {stockton['location']['region']} is {stockton['current']['temp_c']}°C."
)
print("\n- - - - - - - - - - - - - - - - - - -\n")

# What URL would I use to request a 3-day forecast at Heathrow?
days = "3"
forecast_location = "LHR"
query_url = (
    "http://api.weatherapi.com/v1/forecast.json?key="
    + key
    + "&q="
    + forecast_location
    + "&days="
    + days
)
dayloc = requests.get(query_url)
dayloc = dayloc.json()

print(
    f"In order to get a {days}-day forecast at {forecast_location}, you would target the following url:\n{query_url}\n\n"
)
print("\n- - - - - - - - - - - - - - - - - - -\n")

# Print the date of each of the 3 days you're getting a forecast for.
date = []
for day in range(0, 3):
    date.append(dayloc["forecast"]["forecastday"][day]["date"])
print(
    f"Here are the dates that are included in the {days}-day forecast for {forecast_location}:\n{date}\n\n"
)
print("\n- - - - - - - - - - - - - - - - - - -\n")

print("Print the maximum temperature of each of the days.\n")
for day in range(0, 3):
    print(
        f"On {date[day]}, the maximum temperature is forecasted to be {dayloc['forecast']['forecastday'][day]['day']['maxtemp_c']}°C"
    )
print("\n\n")
print("\n- - - - - - - - - - - - - - - - - - -\n")

print("Print the day with the highest maximum temperature.\n")
import statistics
import math

temps = []
for day in range(0, 3):
    temps.append(dayloc["forecast"]["forecastday"][day]["day"]["maxtemp_c"])
max_temp = max(temps)
max_index = temps.index(max_temp)
mean_temp = statistics.mean(temps)
stddev_temp = statistics.stdev(temps)
sqrt_temp = statistics.sqrt(max_temp)
print(
    f"On {date[max_index]}, the maximum temperature is forecasted to be {max_temp}°C.\nThis is the highest temperature in the {days}-day forecast comprising the date range {date[0]} — {date[2]}.\nThe mean temperature for this range is {round(mean_temp, 1)}°C.\nThe standard deviation for this range is {(round(stddev_temp, 1))}.\nThe square root of the maximum temperature from the forecasted range is {sqrt_temp}°C.\nAnd, in case you were wondering, pi times the forecast's maximum temperature raised to the power of its square root is about {round(math.pi * max_temp ** sqrt_temp / 1000000)} million degrees celsius. Dress in layers."
)
