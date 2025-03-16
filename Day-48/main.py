from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = {}

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for n in range(len(event_times)):
    events[n] = {
        "time" : event_times[n].text,
        "name" : event_names[n].text
    }

print(events)


# driver.get("https://www.amazon.com/Emporio-Armani-AR1808-Dress-Silver/dp/B00JGODRKQ/ref=sxin_24_recs_zoco_stores_brand_identity_bs?content-id=amzn1.sym.7d2e00dd-9358-4f89-aca0-04685eb73811%3Aamzn1.sym.7d2e00dd-9358-4f89-aca0-04685eb73811&crid=UB8OGXJQFM8W&cv_ct_cx=emporio+armani+watch+men&keywords=emporio+armani+watch+men&pd_rd_i=B00JGODRKQ&pd_rd_r=d5b0b831-8963-44fe-83a6-0992de6bea24&pd_rd_w=imfww&pd_rd_wg=QbaP8&pf_rd_p=7d2e00dd-9358-4f89-aca0-04685eb73811&pf_rd_r=GAM67CNX3GVXFVY805DX&qid=1741975155&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=emporio%2Caps%2C317&sr=1-3-5f457e4f-4cf5-45bd-948b-58563dcb013a")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is ${price_dollar.text}.{price_cents.text}")
#
# # driver.close() #-> close only active tab
driver.quit() #-> quit from the app

