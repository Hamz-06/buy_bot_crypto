from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import linecache
PATHDRIVER = 'chromedrivers.exe'
#tele id n hash with chat name
api_id = 3743452   #not real 
api_hash = 'f65ae54bdbf263c003de4315b1165de8'   #not real 
channelId = 'https://t.me/bottestmaker'  #tele name chat


def add_ammout():  
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ethInput")))  #locates element on page by id called ethInput. Attemptsd to find element for 10 seconds 

        element.send_keys('0.2')   #enters how much i want to buy 

    finally:
        print("LOCK ARTF")

def submit():
        try:
            button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MuiButton-label")))  #find s element by class 

            button.click()   #cliks on the element 
            
        finally:
            print("LOCK ARTF")     

def refreshpage():  #refreshes the page 
    try:
        redtext = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/span/label/span[2]")))  
        redtext.click()

        confirm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/div/div[2]/button/span[1]")))
        
        confirm.click()
    finally:
        print("LOCK ARTF")

#setrting up chrome optionsd 
teleclient = TelegramClient('sesh',API_ID,API_HASH)

@teleclient.on(events.NewMessage(chats=channelId))
async def my_event_handler(event):
    print(event.raw_text)     #gets cooment from telegram 
    

client.start()
client.run_until_disconnected()
chrome_options = Options()
#chrome settings required for the bot to run 
chrome_options.add_argument('user-data-dir=C:\\Users\\Hamza\Desktop\\boty\\User Data')

chrome_options.add_argument('--profile-directory=Profile 1')

chrome_options.add_argument('disable-infobars')

driver = webdriver.Chrome(PATHDRIVER, options=chrome_options)

driver.get(event.raw_text)  #MAKE SURE YOU CHANGE 

driver.refresh()
time.sleep(0.2)   
try:
    delay = 5
    close_time = time.time()+delay

    while close_time > time.time():

        if (len(driver.window_handles) > 1):

            driver.switch_to.window(driver.window_handles[1])
            # password = driver.find_element_by_id('password')
            # password.send_keys("def")
            # print(len(driver.window_handles))
            action = ActionChains(driver)
            action.send_keys('asdaasda')  # my password (not real)

            action.key_down(Keys.ENTER)
            time.sleep(2)
            action.perform()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            
        else:
            print("Meta Mask did not open, refresh page") # incase of an error 
               
finally:
    print("f")

# completes these said functions in this order 
refreshpage()
    
time.sleep(0.2)

add_ammout()
submit()
