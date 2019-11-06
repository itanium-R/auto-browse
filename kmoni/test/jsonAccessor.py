import requests
import json
import time
import datetime


def loadEEWJson(time=20191106004243): 
  url = "http://www.kmoni.bosai.go.jp/webservice/hypo/eew/"+ str(time) +".json"
  #print(url)
  res = requests.get(url)
  result = json.loads(res.text)
  return result

def calcLocalClockDiff():
  url  = "https://ntp-a1.nict.go.jp/cgi-bin/json"
  res  = requests.get(url)
  ntpT = json.loads(res.text)['st']
  localT = time.time()
  diff = localT - ntpT
  return diff

def getNowStr(diff,offset):
  now  = datetime.datetime.now()
  result = now.strftime('%Y%m%d%H%M%S')
  now -= datetime.timedelta(seconds=int(diff+offset)) 
  result = now.strftime('%Y%m%d%H%M%S')
  return result

def main():
  diff   = calcLocalClockDiff()
  while 1:
    nowStr = getNowStr(diff,3) 
    try:
      eew    = loadEEWJson(nowStr)
      if(eew['report_id']):
        print(eew['report_time'],
              eew['region_name'],
              eew['is_cancel'],
              eew['depth'],
              eew['calcintensity'],     # 震度
              eew['is_final'],
              eew['is_training'],
              eew['magunitude'],        # M
              eew['report_num'],        # 第n報
              eew['request_hypo_type'], 
              eew['report_id'],)        # EEW ID
    except:
      print("connection failed:" + nowStr)
    time.sleep(1)
  
main()
#print(calcLocalClockDiff())

