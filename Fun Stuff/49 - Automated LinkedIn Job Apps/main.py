from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3820814562&f_F=prdm&f_T=27%2C270%2C2995%2C18521&f_WT=2"
           "&keywords=technical%20product%20manager&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
           "&sortBy=R&spellCorrectionEnabled=true")

signin_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
signin_button.click()

email = "john.s.piotrowski@gmail.com"
password = os.environ.get("LI_PW")

email_inputpanel = driver.find_element(By.XPATH, value='//*[@id="username"]')
email_inputpanel.send_keys(email)

pw_inputpanel = driver.find_element(By.XPATH, value='//*[@id="password"]')
pw_inputpanel.send_keys(password)

local_signin_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
local_signin_button.click()


# driver.quit()