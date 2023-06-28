'''
Author: Bram Schork
Date: June, 2023

LET THE DEED SHAW
'''
import json
from config import recipes_path, ingredients_path

# Read recipes JSON data from a file
with open(recipes_path, 'r') as file:
    recipes_data = file.read()

# Parse the recipes JSON data
parsed_recipes = json.loads(recipes_data)

# Read ingredients JSON data from a file
with open(ingredients_path, 'r') as file:
    ingredients_data = file.read()

# Parse the ingredients JSON data
parsed_ingredients = json.loads(ingredients_data)

# Create empty sets to store unique ingredients, unique alcoholic ingredients, and unique glass types
unique_ingredients = set()
unique_alcohol = set()
unique_glasses = set()

# Iterate over each recipe
for recipe in parsed_recipes:
    # Access the values for each recipe
    ingredients = recipe["ingredients"]
    glass = recipe["glass"]

    # Add each ingredient to the unique_ingredients set and check its ABV
    for ingredient in ingredients:
        try:
            ingredient_name = ingredient["ingredient"]
            # unique_ingredients.add(ingredient_name)

            # Check if ingredient information exists in the ingredients JSON
            if ingredient_name in parsed_ingredients:
                ingredient_info = parsed_ingredients[ingredient_name]
                abv = ingredient_info["abv"]
                if abv != 0:
                    unique_alcohol.add(ingredient_name)
                else:
                    unique_ingredients.add(ingredient_name)
        except KeyError:
            pass

    # Add the glass type to the unique_glasses set
    unique_glasses.add(glass)

# Print the unique ingredients, unique alcoholic ingredients, and unique glass types
print("Unique Ingredients:")
for ingredient in sorted(unique_ingredients):
    print(ingredient)

print("\nUnique Alcoholic Ingredients:")
for ingredient in sorted(unique_alcohol):
    print(ingredient)

print("\nUnique Glass Types:")
for glass in sorted(unique_glasses):
    print(glass)
