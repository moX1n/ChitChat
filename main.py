from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("What's the name of the channel would you like the bot to operate in?\n")
print("Make sure you type it correctly!")
selectedChannel = input(">")

driver = webdriver.Firefox()
driver.get("https://www.twitch.tv/popout/{}/chat?popout=".format(selectedChannel))
print("Connecting to: " + driver.title + ".tv/" + selectedChannel)
