from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess
import jtalk
DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver" # selenium driverの保存場所

def uttr(text):
  if text:
    jtalk.jtalk(text)
 
def main():
  chrome  = webdriver.Chrome(DRIVER_PATH)
  url_km  = "http://www.kmoni.bosai.go.jp/"
  buf_text = "initialized text"
  chrome.get(url_km)
               
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
        uttr(ut_text)
        time.sleep(8)
      
main()