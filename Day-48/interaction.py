from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure Chrome webpage
driver = webdriver.Chrome(options=chrome_options)

# To navigate Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(articles.text)

# Find element by link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content Portals")

# Find the "Search" button by <input> by Name
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python", Keys.ENTER)

