import requests
import json

# Получение списка ингредиентов
response = requests.get('https://stellarburgers.education-services.ru/api/ingredients')
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"Total ingredients: {len(data.get('data', []))}")
    
    # Получаем первые 3 ингредиента
    ingredients = data.get('data', [])[:3]
    print("Sample ingredients:")
    for ingredient in ingredients:
        print(f"ID: {ingredient['_id']}, Name: {ingredient['name']}")
    
    # Сохраняем ID ингредиентов в файл
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients]
    print(f"\nIngredient IDs: {ingredient_ids}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)