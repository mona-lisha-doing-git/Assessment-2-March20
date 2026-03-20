from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Automate Resume Upload on Shine Registration Page

Perform the following steps:
- Launch the browser and open the Shine registration page  
- Locate the **Upload Resume** file input field  
- Upload a resume file 

'''

driver.implicitly_wait(15)

driver.get("https://www.shine.com/registration/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='id_file']").send_keys(r"/Users/monalishakalita/Downloads/resume.pdf")

sleep(10)
driver.quit()
