from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = ''  # Download edge driver for your version and replace its path here
driver = webdriver.Edge(PATH)
driver.get("https://web.whatsapp.com/")

# Scan the QR code to login into Whatsapp Web
# Also select the contact to spam
# Then fill in these detail

val = input("Enter the text to spam ")
inp = int(input("Enter no of times to spam "))

time.sleep(10)

input_box = driver.find_elements_by_xpath("//div[@contenteditable='true']")
search = input_box[1]
time.sleep(1)

for index in range(1, inp):
    search.send_keys(val)
    search.send_keys(Keys.RETURN)
    search.send_keys(Keys.RETURN)  # Two times return to send the @ texts properly
