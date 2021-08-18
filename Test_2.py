from selenium import webdriver
import time

#Use Chrome driver
driver = webdriver.Chrome()

#Open Cushman UAT URL
driver.get('https://uat-sitecore-www.cushmanwakefield.com/en')

#Click on Privacy Agreement
Privacy_Agree=driver.find_element_by_xpath('//*[@id="c-p-bn"]')
Privacy_Agree.click()
#close Popup window
LetMeContinue_Button = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/button')

LetMeContinue_Button.click()

Search_Button=driver.find_element_by_xpath(/html/body)
Search_Button.click()

time.sleep(2)
#close the chrome browser
#driver.quit()