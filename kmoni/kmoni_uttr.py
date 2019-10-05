from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import kmoni_common
import time
import subprocess

DRIVER_PATH = "./driver/chromedriver.exe" # selenium driverの保存場所

def main():
  chrome  = webdriver.Chrome(DRIVER_PATH)
  url_km  = "http://www.kmoni.bosai.go.jp/"
  url_ut  = "https://itanium-r.github.io/memorandum/1910wsapi-uttr.html"
  chrome.get(url_km)

  try:
    chrome.execute_script("window.open('','_blank');")
  except:
    print("If it failed to open newtab, please execute again.")

  chrome.switch_to.window(chrome.window_handles[1])
  chrome.get(url_ut)
  chrome.switch_to.window(chrome.window_handles[0])

  kmoni_common.listenEEW(chrome)
  
main()
