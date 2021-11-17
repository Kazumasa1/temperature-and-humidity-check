#!/usr/bin/python3
# -*- coding: utf-8 -*

import datetime #日付ライブラリ読み込み
import Adafruit_DHT #温度センサーライブラリ読み込み
import csv #CSVライブラリの読み込み

#●日付時刻情報の取得--------------------------------------------------------------------

dtime = datetime.datetime.now() #日付、日時の取得
date = dtime.strftime('%Y-%m-%d') #日付の整形 yyyy-mm-dd
time = dtime.strftime('%H:%M') #時間の整形 hh:mm

##---------------------------------------------------------------------------------------

#●センサーの温度を読み込む--------------------------------------------------------------

SENSOR_TYPE = 22 # センサーの種類
DHT_GPIO = 4 # 接続したGPIOポート

# 測定開始
#humidityに湿度を代入
#temperatureに気温を代入
humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, DHT_GPIO)
temperature = "{:.1f}" . format(temperature) #気温（小数点第一位まで）
humidity = "{:.1f}" . format(humidity) #湿度（小数点第一位まで）

##---------------------------------------------------------------------------------------

#●CSVに追記する-------------------------------------------------------------------------

#CSVファイルを末尾追記モード（a）で開く。ファイルが無ければ新規作成してくれる。
#fにファイルを代入 as f:
with open('/home/pi/Documents/DHT22/data.csv','a') as f: 
writer = csv.writer(f) #ファイルfに書き込み
writer.writerow([date,time,temperature,humidity]) #書き込む内容 日時,時間,温度,湿度

##---------------------------------------------------------------------------------------

#追記内容の表示--------------------------------------------------------------------------

print date,time,temperature,humidity

##---------------------------------------------------------------------------------------