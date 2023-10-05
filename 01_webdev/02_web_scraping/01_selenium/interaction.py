# Scraping
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Keep Chrome browser open after program finishes
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)

# Open YouTube in the first tab
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
print(article_count)

search = driver.find_element(By.NAME, "search")
search.send_keys("python", Keys.ENTER)

# Open a new tab
driver.execute_script("window.open('https://secure-retreat-92358.herokuapp.com/', '_blank');")

# Switch to the new tab (Wikipedia)
driver.switch_to.window(driver.window_handles[1])

element = driver.find_element(By.NAME, 'fName')
element.send_keys("D")
element = driver.find_element(By.NAME, 'lName')
element.send_keys("SHR")
element = driver.find_element(By.NAME, 'email')
element.send_keys("dshr@xyz.com")

element = driver.find_element(By.XPATH, '/html/body/form/button')
element.click()
