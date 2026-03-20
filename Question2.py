from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Automate SauceDemo Login and Product Page with Explicit Waits and Verification

'''

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Waiting for the **Username** field to be clickable and entered `"standard_user"`
wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")

# Waiting for the **Password** field to be clickable and entered `"secret_sauce"`
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")

# Waiting for the **Login** button to be clickable and clicked on it
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()

# Captured and printed the page title text
txt = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header_secondary_container']//span[@class='title']")))
print("Page Title Text:", txt.text)


product_names=wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='inventory_item_name ']")))
print("\nALL product names:")
for i in product_names:
    print(i.text)

product_prices=wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='inventory_item_price']")))
print("\nALL product prices:")
for i in product_prices:
    print("$",i.text)

# Click on the fourth product’s **Add to cart** button
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory '])[4]"))).click()

driver.quit()
