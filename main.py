from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = ''
FB_PASSWORD = ''

chrome_driver_path = 'path'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://www.speedtest.net/')

box = driver.find_element_by_class_name('start-text')

box.click()

sleep(20)

down = driver.find_element_by_class_name("download-speed")
down_speed = down.text
up = driver.find_element_by_class_name('upload-speed')
up_speed = up.text


driver.get('https://twitter.com/login')

sleep(19)
email = driver.find_element_by_name('username')
email.send_keys('username')

email.send_keys(Keys.ENTER)
sleep(9)
password = driver.find_element_by_name('password')

password.send_keys('password')
sleep(8)
password.send_keys(Keys.ENTER)

sleep(8)
tweet_compose = driver.find_element_by_class_name('public-DraftStyleDefault-block')

tweet = f"Hey WE Internet, why is my internet speed {down_speed} / {up_speed} up when I pay for {'14 MegaB'} down / {'12 MegaB'} up? \n this is a bot btw "
tweet_compose.send_keys(tweet)
sleep(8)

tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')

tweet_button.click()

sleep(8)
driver.quit()

