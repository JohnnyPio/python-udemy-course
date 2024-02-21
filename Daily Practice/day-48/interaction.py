from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Wikipedia Testing
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # article_count.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.RETURN)

signup_page = driver.get("https://secure-retreat-92358.herokuapp.com/")

fname_inputpanel = driver.find_element(By.NAME, value="fName")
fname_inputpanel.send_keys("John")

lname_inputpanel = driver.find_element(By.NAME, value="lName")
lname_inputpanel.send_keys("Piotrowski")

email_inputpanel = driver.find_element(By.NAME, value="email")
email_inputpanel.send_keys("john.s.piotrowski@gmail.com")

signup_button = driver.find_element(By.CSS_SELECTOR, value="form button")
signup_button.click()

# driver.quit()
