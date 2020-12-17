# 3) Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter 
# for the country a default value. Call your function for three different cities, at least one of which 
# is not in the default country.

################################################################################

def describe_city(city, country = "Merika"): #create a function with two perameters and one perameter is default
    print(f"\nCity of {city.title()} is in {country.title()}") # Displays the city in title case and country in title case

describe_city("Reykjavik", "Iceland") # calling the function 
describe_city("Seattle") # calling the function with one perameter which will display the default second perameter
describe_city("Houston") # calling the function with one perameter which will display the default second perameter
describe_city("London") # calling the function but the default country will not be correct to the city
describe_city("Chang Mai", "Thailand") # calling the function
