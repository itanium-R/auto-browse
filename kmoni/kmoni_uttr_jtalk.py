from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess
import jtalk
import kmoni_common
DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver" # selenium driverの保存場所

def main():
  chrome  = webdriver.Chrome(DRIVER_PATH)
  url_km  = "http://www.kmoni.bosai.go.jp/"
  chrome.get(url_km)
  kmoni_common.listenEEW(chrome)

main()