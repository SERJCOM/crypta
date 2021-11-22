import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_miner = "127.0.0.1"
port_miner = 9093 # информационный порт юзера
sock.bind((ip_miner, port_miner))
general_main_miner_port = 0
info_main_miner_port = 0
dict_listener = 0
dict_miners = 0

sock.sendto(b'RequestToGetMainMiners', ("127.0.0.1", 9090)) # отправить запрос для получения адресов главных майнеров
message, address = sock.recvfrom(1024)
data = message.decode("utf-8")
data = json.loads(data.replace("'",'"'))
print(data)
info_main_miner_port = int(data['port'])

sock.sendto(b'RequestToGetMainPort', (ip_miner, info_main_miner_port)) # отправить запрос для получения основного порта главного майнера 
message, address = sock.recvfrom(1024)
data = message.decode("utf-8")
general_main_miner_port = int(data)
print("основной порт главного майнера ",general_main_miner_port)

sock.sendto(b'RequestToGetListenersAdress', (ip_miner, info_main_miner_port)) # отправить запрос для получения списка слушателей
message, address = sock.recvfrom(1024)
data = message.decode("utf-8")
dict_listener = data
print("словарь слушателей ",dict_listener)

sock.sendto(b'RequestToGetMinersAdress', (ip_miner, info_main_miner_port)) # отправить запрос для получения списка майнеров
message, address = sock.recvfrom(1024)
data = message.decode("utf-8")
dict_miners = data
print("словарь майнеров ",dict_miners)

sock.sendto(b'RequestToSetMode1', (ip_miner, info_main_miner_port)) # отправить запрос для установки режима работы

