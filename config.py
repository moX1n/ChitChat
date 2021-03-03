from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium_cookies import CookieHandler


cookie_choice = input("Load or Save Cookies?\n>") 
dummy_driver = webdriver.Firefox()
cookie_handler = CookieHandler(dummy_driver,"https://twitch.tv",
                               overwrite=False, filename="cooks", wait_time=3)

#   save_cookies() saves the site cookies to the specified file
if cookie_choice.lower() == "save":
    while True:
        dummy_driver.get("https://twitch.tv")
        save_check = input("Login to your account. Once you're logged in, type 'ready' to proceed. \n>")
        if save_check == "ready" or "Ready":
            saved_cookies = cookie_handler.save_cookies()
            print("Refreshed.")
            print("Cookies saved.")
            time.sleep(1)
            dummy_driver.close()
            dummy_driver.quit()
            break;

#   load_cookies() loads the saved cookies from the given file (or the most recently saved one)
if cookie_choice.lower() == "load":
    loaded_cookies = cookie_handler.load_cookies()
    time.sleep(2)
    dummy_driver.refresh()
    print("Refreshed")
    time.sleep(4)
    dummy_driver.close()
    dummy_driver.quit()