from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Amazon
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS")
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
# print(f"The price is: {price_dollar}.{price_cents}")

# By Name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

# By ID
go_button = driver.find_element(By.ID, value="submit")
print(go_button.size)

# By CSS
docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(docs_link.text)

# By XPATH :)
submit_button = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_button.text)

driver.quit()
