from selenium import webdriver
from selenium.webdriver.common.by import By
from type import arr_userName, PASSWORD, LOGIN_URL
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
driver = webdriver.Chrome()
driver.get(LOGIN_URL)
options = Options()

options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

def run_all_users(usernames):
    all_products = [] 
    for username in usernames:
        if login(driver, username, PASSWORD):
            print(f"✅ {username} đăng nhập thành công")
            all_products.extend(extract_products(driver, username))
          
        else:
            print(f"{username} đăng nhập thất bại")
    driver.quit()
    return all_products

def login(driver, username, password):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    return "inventory" in driver.current_url

def extract_products(driver, username):
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    return [
        {
            "Username": username,
            "Product Name": item.find_element(By.CLASS_NAME, "inventory_item_name").text,
            "Price": item.find_element(By.CLASS_NAME, "inventory_item_price").text
        }
        for item in items
    ]
products = run_all_users(arr_userName)
df = pd.DataFrame(products)
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "products1.xlsx")
df.to_excel(downloads_path, index=False)
print("File đã lưu vào:", downloads_path)
print(driver.title)