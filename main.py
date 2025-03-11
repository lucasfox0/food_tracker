import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_APP_KEY"),
    "Content-Type": "application/json"
}

user_input = input("Enter the food description: ")
data = {"query": user_input}

response = requests.post(url, headers=headers, json=data)
response_json = response.json() # Convert the response into a Python dictionary

foods = response_json.get("foods", []) # Retrives the list associated with "foods" key, if it doesn't exist then it defaults to an empty list

if foods: # Ensure that there's at least one food item
    food_name = foods[0].get("food_name", "N/A") # Get the "food_name" key doesn't exist, return "N/A"
    serving_qty = foods[0].get("serving_qty", "N/A") 
    serving_unit = foods[0].get("serving_unit", "N/A")
    calories = foods[0].get("nf_calories", "N/A")
    total_fat = foods[0].get("nf_total_fat", "N/A")
    saturated_fat = foods[0].get("nf_saturated_fat", "N/A")
    total_carbs = foods[0].get("nf_total_carbohydrate", "N/A")
    sugar = foods[0].get("nf_sugars", "N/A")
    protein = foods[0].get("nf_protein", "N/A")

    print(f"Food Name: {food_name}")
    print(f"Serving Quantity: {serving_qty} {serving_unit}")
    print(f"Calories: {calories}")
    print(f"Total Fat: {total_fat}")
    print(f"Saturated Fat: {saturated_fat}")
    print(f"Total Carbohydrates: {total_carbs}")
    print(f"Sugar: {sugar}")
    print(f"Protein: {protein}")
    
else:
    print("No data found.")




# "Pretty print" the JSON
# print(json.dumps(response.json(), indent=2))