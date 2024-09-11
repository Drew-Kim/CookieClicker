from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
# driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/a[1]"))
)

gotIt = driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]")
gotIt.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookie_counter = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookie_counter = int(cookie_counter.replace(",", ""))

    for i in range(4):
        product_price = driver.find_element(
            By.ID, product_price_prefix + str(i)
        ).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookie_counter >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
    # upgrades = driver.find_element(By.CLASS_NAME, "product unlocked enabled")
