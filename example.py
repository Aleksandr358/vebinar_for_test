
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Edge("/Users/kseni/OneDrive/Рабочий стол/ОБУЧЕНИЕ/vebinar_test/msedgedriver")
driver.get("https://google.com")
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]").send_keys('Skillfactory' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
driver.quit()