from selenium_cookies import CookieHandler
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


print("What's the name of the channel would you like the bot to operate in?\n")
print("Make sure you type it correctly!")
selectedChannel = input(">")

driver = webdriver.Firefox()
cookie_handler = CookieHandler(driver,"https://twitch.tv/popout/{}/chat?popout=".format(selectedChannel),
overwrite=False, filename="cooks", wait_time=3)

def chat_options():
    while True:
        desired_string = input("Enter desired string: \n>")
        desired_range = int(input("How many times to spam it? \n>"))
        desired_time = int(input("How long between messages? \n>"))
        for i in range(0, desired_range):
            search = driver.find_element_by_class_name("ScInputBase-sc-1wz0osy-0")
            search.send_keys(desired_string)
            search.send_keys(Keys.RETURN)
            time.sleep(desired_time)
            print(i)

def chat_check():
    print("Initializing... MrDestructoid")
    search = driver.find_element_by_class_name("ScInputBase-sc-1wz0osy-0")
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    search = driver.find_element_by_class_name("ScCoreButtonPrimary-sc-1qn4ixc-1").click()
            
def main():
    
    loaded_cookies = cookie_handler.load_cookies()
    time.sleep(1)
    driver.refresh()
    print("Refreshed Twitch Chat")
    time.sleep(1)
    chat_check()
    chat_options()

main()
