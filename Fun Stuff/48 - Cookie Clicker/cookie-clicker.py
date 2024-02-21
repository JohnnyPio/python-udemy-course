from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, value="cookie")

# Method + cleanup
all_buying_options_container = driver.find_elements(By.CSS_SELECTOR, value="#store")
all_options = [item.text for item in all_buying_options_container]
print(all_options)
raw_list = [item.text.split("\n") for item in all_buying_options_container]
all_buying_options = [val for sublist in raw_list for val in sublist][::2]
prices = [item[item.find("- ") + 2:] for item in all_buying_options]
prices_without_commas = [item.replace(",", "") for item in prices]
prices_as_ints = [int(item) for item in prices_without_commas]

current_time = time.time()
timeout = 5
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    cookie_button.click()
    if time.time() >= current_time + timeout:
        money_amount = int(driver.find_element(By.ID, value="money").text)
        index_to_buy = prices_as_ints.index([item for item in prices_as_ints if item < money_amount][-1])
        print(index_to_buy)
        # TODO - all_buying_options_container isn't a list so I can't reference the index easily to click to buy it...
        all_buying_options_container[index_to_buy].click()
        current_time = time.time()

driver.quit()
