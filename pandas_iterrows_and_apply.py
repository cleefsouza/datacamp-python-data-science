# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print("{}: {}".format(lab, row["cars_per_cap"]))

# Add column

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "Uppercase"] = row["country"].upper()

# Print cars
print(cars)


# Using apply()
cars["Lowercase"] = cars["country"].apply(str.lower)

# Print cars
print(cars)