# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:7])

# Print out observation for Japan
print(cars.loc['JAP']) # .loc
print(cars.iloc[2]) # .iloc

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']]) # .loc
print(cars.iloc[[1, 6]]) # .iloc

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right']) # .loc

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']]) # .loc

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right']) # .loc

# Print out drives_right column as DataFrame
print(cars.iloc[:,[2]]) # .iloc

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0,2]]) # .iloc