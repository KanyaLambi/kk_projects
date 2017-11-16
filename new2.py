from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.get("https://www.gmail.com")
driver.back()

driver.close()