import requests

def fetch_dinner_menu(dining_court, date):
    # Build the API URL
    url = f"https://api.hfs.purdue.edu/menus/v2/locations/{dining_court}/{date}"

    # Make the GET request
    response = requests.get(url)
    menu_data = response.json()

    # Loop through the meals to find 'Dinner'
    dinner_items = []
    for meal in menu_data.get('Meals', []):  # Correctly handle the list of meals
        if meal['Name'] == 'Dinner':  # Check if the meal is Dinner
            dinner_items = meal.get('Stations', [])  # Assuming 'Stations' contain the food items

    # Filter for vegetarian items
    vegetarian_items = []
    for station in dinner_items:  # Loop through each station in dinner
        for item in station.get('Items', []):  # Access items in each station
            if item.get('IsVegetarian'):  # Check if the item is vegetarian
                vegetarian_items.append(item['Name'])

    return vegetarian_items

# Example use
dining_court = "Ford"
date = "04-14-2024"
vegetarian_dinner_menu = fetch_dinner_menu(dining_court, date)
print()
print(f"There are {len(vegetarian_dinner_menu)} VEGETARIAN options at {dining_court} on {date} dinner:")
print(vegetarian_dinner_menu)
print()
print("Vegetarian Dinner Menu Items:")
for item in vegetarian_dinner_menu:
    print(item)


########################################################################################################

### SAMPLE OUTPUT DATAPROCESSING:

# There are 36 VEGETARIAN options at Ford on 04-14-2024 dinner:
# ['Battered Cauliflower', 'Honey Mustard Dressing', "Frank's Red Hot Buffalo Sauce", 'Hidden Valley Ranch Dressing', 'Celery Sticks', 'Baby Carrots', "Ken's Cannonball BBQ Sauce", 'Honey BBQ Wing Sauce', 'Hickory Smoke BBQ Sauce', 'Honey Chipotle Wing Sauce', 'Moroccan Dried Fruit and Nut Couscous', 'Pita Folds', 'Greek Potatoes', 'Tzatziki Sauce', 'Shredded Lettuce', 'Diced Tomatoes', 'Diced Onion', 'Crumbled Feta Cheese', 'Roasted Brussels Sprouts', 'Potato Chips', 'Snickerdoodle Cookie', 'Fruits of the Forest Pie', 'Moroccan Dried Fruit and Nut Couscous', 'Roasted Brussels Sprouts', 'Mango Chunks', 'Applesauce', 'Malibu Burger', 'GF White Bread', 'GF Hamburger Bun', 'Vegan Shredded Mozzarella Cheese', 'GF Cauliflower Pizza Crust', 'GF Double Chocolate Muffin', 'GF Blueberry Muffin', 'Homefree Chocolate Chip Brownie', 'Homefree Chocolate Chip Cookie', 'Homefree Ginger Snap Cookie']

# Vegetarian Dinner Menu Items:
# Battered Cauliflower
# Honey Mustard Dressing
# Frank's Red Hot Buffalo Sauce
# Hidden Valley Ranch Dressing
# Celery Sticks
# Baby Carrots
# Ken's Cannonball BBQ Sauce
# Honey BBQ Wing Sauce
# Hickory Smoke BBQ Sauce
# Honey Chipotle Wing Sauce
# Moroccan Dried Fruit and Nut Couscous
# Pita Folds
# Greek Potatoes
# Tzatziki Sauce
# Shredded Lettuce
# Diced Tomatoes
# Diced Onion
# Crumbled Feta Cheese
# Roasted Brussels Sprouts
# Potato Chips
# Snickerdoodle Cookie
# Fruits of the Forest Pie
# Moroccan Dried Fruit and Nut Couscous
# Roasted Brussels Sprouts
# Mango Chunks
# Applesauce
# Malibu Burger
# GF White Bread
# GF Hamburger Bun
# Vegan Shredded Mozzarella Cheese
# GF Cauliflower Pizza Crust
# GF Double Chocolate Muffin
# GF Blueberry Muffin
# Homefree Chocolate Chip Brownie
# Homefree Chocolate Chip Cookie
# Homefree Ginger Snap Cookie

  

### SAMPLE OUTPUT API:  (On CLI: curl -v -L https://api.hfs.purdue.edu/menus/v2/locations/Earhart/04-13-2024)

# {
# "Location":"Earhart",
# "Date":"4/13/2024",
# "IsPublished":true,
# "Notes":"A dining court supervisor can provide allergen information for menu offerings not posted in the app.",
# "Meals":[{
#   "ID":"e4369879-fac9-4c96-ac11-5c3bde016188",
#   "Name":"Breakfast",
#   "Order":0,
#   "Status":"Closed",
#   "Type":"Breakfast",
#   "Hours":null,
#   "Notes":null,
#   "Stations":[]
#   },

#   {"ID":"d22f2a83-7043-446e-a11f-dddd97c13db3",
#   "Name":"Lunch",
#   "Order":1,
#   "Status":"Open",
#   "Type":"Lunch",
#   "Hours":{"StartTime":"10:00:00","EndTime":"14:00:00"},
#   "Notes":null,
#   "Stations":[{
#     "Name":"Granite Grill",
#     "Items":[{
#       "ID":"a450b59f-717e-4cf5-a60e-347154816307",
#       "Name":"Polish Sausage",
#       "IsVegetarian":false,
#       "NutritionReady":true,
#       "Allergens":[	{"Name":"Coconut","Value":false},
#           {"Name":"Eggs","Value":false},
#           {"Name":"Fish","Value":false},
#           {"Name":"Gluten","Value":false},
#           {"Name":"Milk","Value":false},
#           {"Name":"Peanuts","Value":false},
#           {"Name":"Sesame","Value":false},
#           {"Name":"Shellfish","Value":false},
#           {"Name":"Soy","Value":false},
#           {"Name":"Tree Nuts","Value":false},
#           {"Name":"Vegetarian","Value":false},
#           {"Name":"Vegan","Value":false},
#           {"Name":"Wheat","Value":false}
#             ]
#       },
#       {
#       "ID":"60d9accc-195f-4514-9530-7da1c08b7d82",
#       "Name":"Super Beef Hot Dog",
#       "IsVegetarian":false,
#       "NutritionReady":true,
#       "Allergens":[	{"Name":"Coconut","Value":false},
#           {"Name":"Eggs","Value":false},
#           {"Name":"Fish","Value":false},
#           {"Name":"Gluten","Value":false},
#           {"Name":"Milk","Value":false},
#           {"Name":"Peanuts","Value":false},
#           {"Name":"Sesame","Value":false},
#           {"Name":"Shellfish","Value":false},
#           {"Name":"Soy","Value":false},
#           {"Name":"Tree Nuts","Value":false},
#           {"Name":"Vegetarian","Value":false},
#           {"Name":"Vegan","Value":false},
#           {"Name":"Wheat","Value":false}
#             ]
#       },
#       {...
#       }
#     }]
#   }]
# }




########################################################################################################
