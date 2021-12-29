import socket
import json

ip_main_miner = "127.0.0.1"
port_main_miner_info = 9091 # информационный порт главного майнера
port_main_miner = 9092 # основной порт главного майнера

sock_info = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_info.bind((ip_main_miner, port_main_miner_info))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_main_miner, port_main_miner))

dict_listener = []
dict_miners = []

while True:
    message, address = sock_info.recvfrom(1024)
    data = message.decode("utf-8")
    print(dict_listener)
    print(data)
    if data == "RequestToGetMainPort":
        answer  = json.dumps(port_main_miner).encode('utf-8')
        sock_info.sendto(answer, address)
    if data == "RequestToGetListenersAdress":
        answer  = json.dumps(dict_listener).encode('utf-8')
        sock_info.sendto(answer, address)
    if data == "RequestToGetMinersAdress":
        answer  = json.dumps(dict_miners).encode('utf-8')
        sock_info.sendto(answer, address)
    if data == "RequestToSetMode1": # режим 1 - слушатель
        dict_listener.append(address)
        print("словарь слушателей ",dict_listener)
    if data == "RequestToSetMode2": # режим 2 - майнер
        dict_miners.append(address)
        print("словарь майнеров ",dict_miners)
    

