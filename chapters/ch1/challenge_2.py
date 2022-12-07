# 1. Ask user their season of the year
season_of_year = input('Enter your season of the year: ')

# 2. Ask user their number of choice
favorite_number = input('Enter your favorite number: ')

# 3. Ask user their preference of Adjective
adj_preference = input('Enter your favorite adjective')

# 4. Print the entries with the format of 'On a[adjective][season] day, i drink at least [number] cups of juice'
print(f'On a {adj_preference} {season_of_year} day, I drink at least {favorite_number} cups of juice!')