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
driver.get("https://orteil.dashnet.org/experiments/cookie")

button = driver.find_element(By.XPATH, '//*[@id="cookie"]')
for i in range(1000):
    button.click()

