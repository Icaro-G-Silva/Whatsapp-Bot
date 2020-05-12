from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


def verifyInput(message, sendTo):
    if type(message) != str or type(sendTo) != list:
        raise Exception(f"Invalid format for message:{type(message)} or sendTo:{type(sendTo)}\nNeed to be message:{str} and sendTo:{list}")

def verifyTimeInput(hour, minute):
    if type(hour) != int or type(minute) != int:
        raise Exception(f"Invalid format for hour:{type(hour)} or minute:{type(minute)}\nNeed to be hour:{int} and minute:{int}")
    if hour > 23 or hour < 0:
        raise Exception(f"Hour:{hour} is not suitable to hour pattern 0 - 23")
    elif minute > 59 or minute < 0:
        raise Exception(f"Minute:{minute} is not suitable to minute pattern 0 - 59")

def wait(seconds):
    time.sleep(seconds)


class WhatsappBot:
    def __init__(self, message, sendTo):
        verifyInput(message, sendTo)
        self.message = message
        self.sendTo = sendTo
        self.cooldown = (0.005 * len(self.message))
        self.time = [False, False]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    
    def connectToWhatsapp(self):
        self.driver.get("https://web.whatsapp.com/")
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "pane-side")))
        except:
            raise Exception("Take too time to load the page.")
    
    def scheduleTime(self, hour = datetime.now().hour, minute = datetime.now().minute):
        verifyTimeInput(hour, minute)
        self.time = [hour, minute]
    
    def verifyTime(self):
        if not self.time[0] and not self.time[1]: return
        while True:
            time = datetime.now()
            if time.hour == self.time[0] and time.minute == self.time[1]: return

    def sendMessages(self, isFlood = False):
        if not isFlood:
            self.connectToWhatsapp()
            self.verifyTime()
        for contact in self.sendTo:
            contacts = self.driver.find_element_by_xpath(f"//span[@title='{contact}']")
            wait(self.cooldown)
            contacts.click()
            chatBox = self.driver.find_element_by_class_name("_1Plpp")
            wait(self.cooldown)
            chatBox.click()
            chatBox.send_keys(self.message)
            sendButton = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            wait(self.cooldown)
            sendButton.click()
            wait(self.cooldown + 0.2)

    def sendFlood(self, times):
        self.connectToWhatsapp()
        self.verifyTime()
        for _ in range(0, times):
            self.sendMessages(True)
