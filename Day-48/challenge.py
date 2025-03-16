from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure Chrome webpage
driver = webdriver.Chrome(options=chrome_options)

# To navigate Wikipedia
driver.get("http://secure-retreat-92358.herokuapp.com")

# Filling the First and Last Names and Email Address
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Random")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Generator")

email = driver.find_element(By.NAME, value="email")
email.send_keys("randomgenerator@test.com")

# Pressing the Sign Up Button
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.send_keys(Keys.ENTER)
