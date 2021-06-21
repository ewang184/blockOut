import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


words = open("./badwords.txt", "r")

stringOf = words.read()

inListForm = re.split(", *", stringOf)

driver = webdriver.Chrome('./chromedriver')
actions = ActionChains(driver)
driver.get("https://discord.com/login")

username = driver.find_element_by_name("email")
pword = driver.find_element_by_name("password")

username.send_keys("dummyusername")
pword.send_keys("dummypass")
pword.send_keys(Keys.RETURN)
while (driver.current_url != "https://discord.com/channels/@me"):
	time.sleep(1)

if driver.current_url=="https://discord.com/channels/@me":
	print("reached")
	driver.get("dummydiscordchannel")
time.sleep(10)

actions.send_keys("video")
while(True):
    time.sleep(1)
    messages = driver.find_elements_by_css_selector("")

    mostRecent = (messages[len(messages)-1].text)

    listBadWords = re.split("\s", mostRecent)

    if(listBadWords[0]=="censorThis"):
        for k in range(len(listBadWords)-1):
            if(listBadWords[k+1] != "VIDEO"):
                inListForm.append(listBadWords[k+1])
                tempo = open("./badwords.txt", "a")
                tempo.write(", "+listBadWords[k+1])
                tempo.close()
        print("censored")

    if(listBadWords[0]=="uncensorThis"):

    for i in range(len(listBadWords)):
        for j in range(len(inListForm)):
            print(i)
            print(j)
            print(len(listBadWords))
            print(listBadWords[i])
            print(inListForm[i])

            if (listBadWords[i] == inListForm[j]):
                print("bad word detected")                
                actions.perform()
                actions.perform()

            else:
                print("all clear")
