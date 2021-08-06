#BITSO API CLIENT
import time
import requests
import pandas as pd
import matplotlib as plt
import mysql.connector
from datetime import datetime

bitso_url_prod = 'https://api.bitso.com/v3/'
bitso_url_dev  = 'https://api-dev.bitso.com/v3/'


crypVsBTC = {
  "BTC": "btc_mxn",
  "ETH": "eth_btc",
  "XRP": "xrp_btc",
  "LTC": "ltc_btc",
  "BCH": "bch_btc",
  "TUSD": "tusd_btc",
  "MANA": "mana_btc",
  "BAT": "bat_btc",
  "DAI": "btc_dai",
  "ARS": "btc_ars"
}

crypVsMXN = {
  "BTC": "btc_mxn",
  "ETH": "eth_mxn",
  "XRP": "xrp_mxn",
  "LTC": "ltc_mxn",
  "BCH": "bch_mxn",
  "TUSD": "tusd_mxn",
  "MANA": "mana_mxn",
  "BAT": "bat_mxn",
  "DAI": "dai_mxn"
}

crypVsUSD = {
  "BTC": "btc_usd",
  "ETH": "eth_usd",
  "XRP": "xrp_usd"
}

hostname = 'localhost'
username = 'root'
password = 'root'
database = 'bitso_client_db'


def getAvailableBooks():
    print('Consultando precios en general')
    resp = requests.get(bitso_url_prod+'available_books/')
    print('Codigo de Respuesta = ',resp.status_code)

    if resp is not None:
        data = resp.json()  

        if data.get('success'):
            return data.get('payload')
        else:
            return 'Error ' + resp.status_code
    else:
        return 'Sin información'

def getTicker(crypto):
    
    print('Consultando precio actual de', crypto)
    resp = requests.get(bitso_url_prod+'ticker/?book='+crypto)
    print('Codigo de Respuesta = ',resp.status_code)

    if resp is not None:
        data = resp.json()  
        if data.get('success'):
            return data.get('payload')
        else:
            return 'Error ' + resp.status_code

    else:
        return 'Sin información'




def db_getBTC_HIST() :

    conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
    cur = conn.cursor()

    cur.execute( "SELECT * FROM bitcoin_hist" )

    for x in cur:
        print(x)

    conn.close()

def db_postBTC_HIST(btc_ticker) :

    conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
    cur = conn.cursor()

    today_raw = datetime.now()
    today = today_raw.strftime("%Y-%m-%d %H:%M:%S")

    cur.execute(
        "INSERT INTO bitcoin_hist (high,last,created_at,volume,vwap,low,ask,bid,change_24,fecha) VALUES (%s,%s,%s, %s,%s,%s, %s,%s,%s,%s)", 
        (btc_ticker.get('high'),btc_ticker.get('last'),btc_ticker.get('created_at'),btc_ticker.get('volume'),btc_ticker.get('vwap'),
        btc_ticker.get('low'),btc_ticker.get('ask'),btc_ticker.get('bid'),btc_ticker.get('change_24'), today)
    )
    conn.commit()

    conn.close()

def procedure():
   time.sleep(1.1)

i=0
while(i < 100 ):
    # measure wall time
    t1 = time.time()
    procedure()
    print (time.time() - t1, "seconds wall time")
    i = i + 1 

    btc_ticker = getTicker(crypVsMXN.get('BTC'))
    #Valor Dummy
    #btc_ticker = {'high': '812000.00', 'last': '798838.36', 'created_at': '2021-07-28T20:50:58+00:00', 'book': 'btc_mxn', 'volume': '156.01037981', 'vwap': '789583.6671273016', 'low': '756000.00', 'ask': '799379.42', 'bid': '798421.17', 'change_24': '41600.20'}
    db_postBTC_HIST(btc_ticker)
    print ("Obteniendo consulta precion BTC (%s,%s), iteracion -> %s" % (btc_ticker.get('high'),btc_ticker.get('low'),i))

