from selenium import webdriver
import time
import os

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/?logout=1609165116251"
CHROME_DRIVER = "/Users/shubham/Development/chromedriver"
TWITTER_USERNAME = os.environ.get('TWITTER_USERNAME')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')

required_downspeed = int(input("Enter required download speed in mbps: "))
required_upspeed = int(input("Enter required upload speed in mbps: "))

driver = webdriver.Chrome(CHROME_DRIVER)

driver.get(SPEED_TEST_URL)
time.sleep(2)
go = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go.click()

time.sleep(60)

down_speed = round(float(driver.find_element_by_class_name("download-speed").text), 2)
up_speed = round(float(driver.find_element_by_class_name("upload-speed").text), 2)

print(down_speed, up_speed)

if down_speed < required_downspeed or up_speed < required_upspeed:

    driver.get(TWITTER_URL)

    time.sleep(2)

    # log_in = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
    log_in = driver.find_element_by_xpath('//a[@href="/login"]')
    log_in.click()

    time.sleep(2)

    mobile = driver.find_element_by_name("session[username_or_email]")
    mobile.send_keys(TWITTER_USERNAME)
    password = driver.find_element_by_name("session[password]")
    password.send_keys(TWITTER_PASSWORD)

    log_in = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')

    log_in.click()

    time.sleep(5)

    get_started_close = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg/g/path')
    get_started_close.click()



    tweet_text = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    tweet_text.send_keys(f"Hey @my_service_provider, My download speed: {down_speed}mbps⬇️, upload speed: {up_speed}mbps⬆️. "
                         f"It should be {required_downspeed}⬇️/{required_upspeed}⬆️. Please help.")

    tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
    tweet.click()



driver.quit()