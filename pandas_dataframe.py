# In the exercises that follow you will be working with vehicle data from different countries.
# Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

# Three lists are defined in the script:

# names, containing the country names for which data is available.
# dr, a list with booleans that tells whether people drive left or right in the corresponding country.
# cpc, the number of motor vehicles per 1000 people in the corresponding country.

# Each dictionary key is a column label and each value is a list which contains the column elements.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names,
    'drives_right':dr,
    'cars_per_cap':cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)