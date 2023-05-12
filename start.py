from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telebot
from telebot import types

token = "TOKEN" # Telegram Bot Token

bot = telebot.TeleBot(token, parse_mode=None)
u_chat_id = 2102357422 # Telegram Chat ID

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/cna_adam/")

time.sleep(7)
current_profile_pic = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/div/div/span/img").get_attribute("src")
while True:
    driver.refresh()
    time.sleep(3)
    new_profile_pic = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/main/div/header/div/div/span/img").get_attribute("src")
    if new_profile_pic != current_profile_pic:
        print("Profil fotoğrafı değiştirildi!")
        bot.send_message(u_chat_id, "Profil fotoğrafı değiştirildi! " + new_profile_pic)
        current_profile_pic = new_profile_pic
    time.sleep(60)
