import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests




import requests


api_key = 'e430bdacdcc84f00893a16e0404019a7'
ingredients = 'apple,flour,sugar'
url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}'

response = requests.get(url)
recipes = response.json()

for recipe in recipes:
       title = recipe['title']
       image = recipe['image']
       print(f'Название рецепта: {title}')
       print(f'Ссылка на изображение: {image}')

try:
    #инициализирую драйвер
    driver = webdriver.Chrome()
    #говорим WebDriver каждый элемент искать 5 секунд.
    # путь до страницы
    driver.get('https://erikdark.github.io/recept_api/')

a='Cranberry Apple Crisp'
img='https://img.spoonacular.com/recipes/640352-312x231.jpg'
#y= driver.find./element(results)
#c= driver.find./element(results)
#if a=y
#b= c
 if driver.find_element(By.ID,'results').text == 'Recipe: Cranberry Apple Crisp':
        print('ok')
    else:
        print('ne okey')