from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://messages.google.com/web/")

#input("Press anything after QR scan")
time.sleep(15)

names = [''] #Enter the contact names

Message = "Hey, This is Bot of T3cH_W1z4rD" #Enter the Message

for name in names:
    driver.maximize_window()
    driver.find_element_by_xpath("//span/div[2]").click() #Click on Search contacts button
    time.sleep(3)
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").clear() #Locate and clear Searchbox
    driver.find_element_by_xpath("//input[@placeholder='Type a name, phone number, or email']").send_keys(name) #Type contact name
    time.sleep(7)
    driver.find_element_by_xpath("//mw-contact-row/div/div/div[2]").click() #Click on first contact
    time.sleep(7)
    try:
        driver.find_element_by_xpath("//textarea[@placeholder='Text message from BSNL MOBILE']").clear() #Locate and clear message box
        time.sleep(7)
        driver.find_element_by_xpath("//textarea[@placeholder='Text message from BSNL MOBILE']").send_keys(Message) #Type the message in message box
        time.sleep(7)
    except:
        driver.find_element_by_xpath("//textarea[@placeholder='Text message from JIO']").clear() #Locate and clear message box
        time.sleep(7)
        driver.find_element_by_xpath("//textarea[@placeholder='Text message from JIO']").send_keys(Message) #Type the message in message box
        time.sleep(7)
    driver.find_element_by_xpath("//mws-message-compose/div/mws-message-send-button/button/span").click() #Click on Send button
#driver.quit()
print("Message Sent Successfully....")
