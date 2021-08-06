import websocket #websocket-client library
import json

#websocket.enableTrace(True)

socket = 'wss://ws.bitso.com'

def on_open(ws):
    print("------ Opened ------")

    get_data_trades = { 'action': 'subscribe', 'book': 'btc_usd', 'type': 'trades' }
    get_data_diff_orders = { 'action': 'subscribe', 'book': 'btc_usd', 'type': 'diff-orders' }
    get_data_orders = { 'action': 'subscribe', 'book': 'btc_usd', 'type': 'orders' }
    ws.send(json.dumps(get_data_trades))
    ws.send(json.dumps(get_data_diff_orders))
    ws.send(json.dumps(get_data_orders))

def on_message(ws, message):
    message = json.loads(message)

    if message['type'] == 'trades' and "payload" in message:
        print('TRADES: ', message['payload'])

    elif message['type'] == 'diff-orders' and message['payload']:
        print('DIFF-ORDERS: ', message['payload'])

    elif message['type'] == 'orders' and message['payload']:
        print('ORDERS: ', message['payload'])

    elif message['type'] == 'ka':
        print('ALIVE: ', message)

    else:
        print('MESSAGE: ', message)

def on_close(ws, close_status_code, close_msg):
    print("----Closed connection----")
    # Because on_close was triggered, we know the opcode = 8
    if close_status_code or close_msg:
        print("on_close args:")
        print("close status code: ", str(close_status_code))
        print("close message: ", str(close_msg))

def on_error(ws, error):
    print(error)

websocket.enableTrace(True)              
ws = websocket.WebSocketApp(socket, 
                            on_open=on_open, 
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)     


ws.run_forever()



#++Rcv decoded: fin=1 opcode=1 data=b'{"action":"subscribe","response":"ok","time":1628194353950,"type":"trades"}'
#++Rcv decoded: fin=1 opcode=1 data=b'{"type":"trades","book":"btc_usd","payload":[{"i":43293551,"a":"0.0168","r":"40928.89","v":"687.605352","mo":"yRdfs2xsNKDA3skF","to":"AWXYQDPRxfZIVLbB","t":0}]}'