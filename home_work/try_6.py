from selenium import webdriver
from selenium.webdriver.common.by import By

def test_elements_exist(username, password, submit):

    driver = webdriver.Chrome() # нужно прописать путь до драйвера, если его нет в корне проекта
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR)
    password = driver.find_element(By.CSS_SELECTOR)
    submit = driver.find_element(By.CSS_SELECTOR)

    if username is None and password is None and submit is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')


