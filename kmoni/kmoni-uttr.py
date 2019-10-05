from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess
DRIVER_PATH = "./driver/chromedriver.exe" # selenium driverの保存場所

def uttr(chrome,text):
  if text:
    chrome.switch_to.window(chrome.window_handles[1])
    chrome.find_element_by_id("text").clear()
    chrome.find_element_by_id("text").send_keys(text)
    chrome.find_element_by_id("uttrBtn").click()
    chrome.switch_to.window(chrome.window_handles[0])
  
def main():
  chrome  = webdriver.Chrome(DRIVER_PATH)
  url_km  = "http://www.kmoni.bosai.go.jp/"
  url_ut  = "https://itanium-r.github.io/memorandum/1910wsapi-uttr.html"
  buf_text = "initialized text"
  chrome.get(url_km)

  chrome.execute_script("window.open('','_blank');")
  chrome.switch_to.window(chrome.window_handles[1])
  chrome.get(url_ut)
  chrome.switch_to.window(chrome.window_handles[0])
  while 1:
    time.sleep(1)
    text=chrome.find_element_by_id("main-message").text
    if buf_text != text:
      print(text)
      buf_text = text
      if text:
        ut_text  = chrome.find_element_by_id("map-message-area").text
        ut_text += "で最大震度"
        ut_text += chrome.find_element_by_id("map-message-sindo-value").text
        ut_text += "の地震発生。"
        ut_text += chrome.find_element_by_id("map-message-value").text
        ut_text  = ut_text.replace('M','マグニチュード').replace('\n',' ')
        uttr(chrome,ut_text)
        time.sleep(6)
      
main()
