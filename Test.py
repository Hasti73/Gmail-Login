from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#navigate to the url  
driver.get('http://www.gmail.com')

#maximize the window size  
driver.maximize_window()

#identify the user name text box and enter the value 
driver.find_element_by_id("identifierId").send_keys("tlogin073")

#click on the next button  
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()

wait = WebDriverWait(driver, 100)
element = wait.until(EC.element_to_be_clickable((By.ID, "password")))
#identify the password text box and enter the value   
driver.find_element_by_name("password").send_keys("ADRFIUYV23456")

#click on the next button  
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

wait = WebDriverWait(driver, 10)

