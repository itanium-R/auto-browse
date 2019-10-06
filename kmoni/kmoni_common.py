from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import subprocess
import jtalk

def uttr_websp(chrome,text):
  if text:
    print(text)  
    chrome.switch_to.window(chrome.window_handles[1])
    chrome.find_element_by_id("text").clear()
    chrome.find_element_by_id("text").send_keys(text)
    chrome.find_element_by_id("uttrBtn").click()
    chrome.switch_to.window(chrome.window_handles[0])

def uttr(ut_text,ut_way,chrome):  
  if ut_way == "jtalk":
    jtalk.jtalk(ut_text)
  elif ut_way == "websp":
    uttr_websp(chrome,ut_text)
  else:
    print("invalid utter way")


def listenEEW(chrome,ut_way):
  while 1:
    time.sleep(1)
    text = chrome.find_element_by_id("main-message").text
    if text:
      area = chrome.find_element_by_id("map-message-area").text
      ut_text  = buf_area = area
      ut_text += "で最大震度"
      ut_text += chrome.find_element_by_id("map-message-sindo-value").text
      ut_text += "の地震発生。"
      # ut_text += chrome.find_element_by_id("map-message-value").text
      uttr(ut_text,ut_way,chrome)
      buf_shindo = ""
      buf_mag    = ""
      buf_depth  = ""
      buf_m_num  = ""

      while 1:
        time.sleep(3)
        m_num = chrome.find_element_by_id("map-message-num").text
        
        if buf_m_num == m_num:
          continue
        
        print(m_num)
        buf_m_num = m_num
        area = chrome.find_element_by_id("map-message-area").text

        if buf_area != area:
          break

        text   = chrome.find_element_by_id("main-message").text
        shindo = chrome.find_element_by_id("map-message-sindo-value").text
        mag    = chrome.find_element_by_id("map-message-mag-value").text
        depth  = chrome.find_element_by_id("map-message-depth-value").text
        ut_text= ""

        if buf_shindo != shindo:
          ut_text += " 最大震度" + shindo
          buf_shindo = shindo
        
        if buf_mag != mag:
          ut_text += " マグニチュード" + mag
          buf_mag = mag
        
        if buf_depth != depth:
          ut_text += " 深さ" + depth
          buf_depth = depth
          uttr(ut_text,ut_way,chrome)