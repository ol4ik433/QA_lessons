import requests


url = 'https://api.unsplash.com/photos/'
query={"nature"}
#q = {"city name":'London'}
#appid={"d5b6760ee55b6f35b8a3ce79962e1575"}
response = requests.get(url,params=query)


print(response.url)
print(response.json())





        #driver.find_element(By.ID,'verify').click()


       # WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.ID,'verify_message')))




       # assert driver.find_element(By.ID,'verify_message').text == 'Verification successful!','текст должен быть Verification successful!'