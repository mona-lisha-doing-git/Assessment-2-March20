from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Automate Data Extraction from Pro Kabaddi Standings

* Matches Played
* Won
* Lost
* Score Difference (Diff)
* Points

'''

driver.implicitly_wait(15)

driver.get("https://www.prokabaddi.com")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@title='Standings']").click()

matches_played = driver.find_element(By.XPATH, "//div[contains(p, 'Jaipur')]/../../..//div[@class='table-data matches-play']")
print("Matches Played:", matches_played.text)

matches_won = driver.find_element(By.XPATH, "//div[contains(p, 'Jaipur')]/../../..//div[@class='table-data matches-won']")
print("Matches Won:", matches_won.text)

matches_lost = driver.find_element(By.XPATH, "//div[contains(p, 'Jaipur')]/../../..//div[@class='table-data matches-lost']")
print("Matches Lost:", matches_lost.text)

score_diff = driver.find_element(By.XPATH, "//div[contains(p, 'Jaipur')]/../../..//div[@class='table-data score-diff']")
print("Score Difference (Diff):", score_diff.text)

points = driver.find_element(By.XPATH, "//div[contains(p, 'Jaipur')]/../../..//div[@class='table-data points']")
print("Points:", points.text)

sleep(10)
driver.quit()
