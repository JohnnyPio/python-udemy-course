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


def get_prices(options):
    raw_list = [item.text.split("\n") for item in options][:-1]
    all_buying_options = [val for sublist in raw_list for val in sublist]
    prices = [item[item.find("- ") + 2:] for item in all_buying_options]
    prices_without_commas = [item.replace(",", "") for item in prices]
    final_prices = [int(item) for item in prices_without_commas]
    return final_prices


start_time = time.time()
timeout = 5
end_game = 30
game_is_on = True
while game_is_on:
    current_time = start_time
    time.sleep(0.05)
    cookie_button.click()

    if time.time() >= start_time + end_game:
        game_is_on = False
        print(driver.find_element(By.ID, value="cps").text)
        break

    if time.time() >= current_time + timeout:
        money_amount = int(driver.find_element(By.ID, value="money").text)
        all_buying_options_container = driver.find_element(By.CSS_SELECTOR, value="#store")
        all_options = all_buying_options_container.find_elements(By.TAG_NAME, value="b")

        prices_as_ints = get_prices(all_options)
        if money_amount > prices_as_ints[0]:
            last_index = [item for item in prices_as_ints if item < money_amount][-1]
            index_to_buy = prices_as_ints.index(last_index)
            all_options[index_to_buy].click()
        current_time = time.time()

driver.quit()
