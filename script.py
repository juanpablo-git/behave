from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.profsandromesquita.com/")
ul = driver.find_element(By.CSS_SELECTOR,"#h\.74942282c9d6894a_16 > div:nth-child(1) > div:nth-child(1) > ul:nth-child(3)")


li = ul.find_elements(By.CSS_SELECTOR,"li")
for l in li:
    l.click()
    
for i in driver.window_handles:
    time.sleep(3)
    driver.switch_to.window(i)
    time.sleep(3)
    print(driver.current_url," -->> ",requests.get("https://ifce.edu.br/").status_code)
    time.sleep(3)

    




