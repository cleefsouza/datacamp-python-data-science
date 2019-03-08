# The data is available in a CSV file, named cars.csv.
# It is available in your current working directory, so the path to the file is simply 'cars.csv'.

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
# Fix import by including index_col
cars = pd.read_csv("cars.csv", index_col = 0)

# Print out cars
print(cars)