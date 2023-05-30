from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@given('acessando o site do sandro')
def step_impl(context):
    driver.get("https://www.profsandromesquita.com/")
    

@when('acessando os links')
def step_impl(context):
    ul = driver.find_element(By.CSS_SELECTOR,"#h\.74942282c9d6894a_16 > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3)")

    li = ul.find_elements(By.CSS_SELECTOR,"li")

    for l in li:
        l.click()
    
    
    
    assert True is not False

@then('verificando se as paginas estão ativas')
def step_impl(context):
    for i in driver.window_handles:
        time.sleep(3)
        driver.switch_to.window(i)
        time.sleep(3)
        code = requests.get(driver.current_url).status_code
        time.sleep(3)
        assert code != 404


