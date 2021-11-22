import socket
import json


class Listener:
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_miner = "127.0.0.1"
    port_miner = 9093 # информационный порт юзера
    sock.bind((ip_miner, port_miner))
    general_main_miner_port = 0
    info_main_miner_port = 0
    dict_listener = 0
    dict_miners = 0
    message = 0
    adress = 0

    def SendRequest(self, ip, port, message):
        print(ip, port, message)
        self.sock.sendto(message, (ip, port))

    def SendRequestToGetMainMiners(self):                       # отправить запрос для получения адресов главных майнеров
        self.SendRequest("127.0.0.1", 9090, b"RequestToGetMainMiners")
        message, address = self.sock.recvfrom(1024)
        data = message.decode("utf-8")
        data = json.loads(data.replace("'",'"'))
        self.info_main_miner_port = int(data['port'])

    def SendRequestToGetMainPort(self):
        self.SendRequest(self.ip_miner, self.info_main_miner_port, b"RequestToGetMainPort")
        message, address = self.sock.recvfrom(1024)
        data = message.decode("utf-8")
        self.general_main_miner_port = int(data)
        print("основной порт главного майнера ",self.general_main_miner_port)

    def SendRequestToGetListenersAdress(self):                  # отправить запрос для получения списка слушателей
        self.SendRequest(self.ip_miner, self.info_main_miner_port, b"RequestToGetListenersAdress")
        message, address = self.sock.recvfrom(1024)
        data = message.decode("utf-8")
        self.dict_listener = data
        print("словарь слушателей ",self.dict_listener)

    def SendRequestToGetMinersAdress(self):                     # отправить запрос для получения списка майнеров
        self.SendRequest(self.ip_miner, self.info_main_miner_port, b"RequestToGetMinersAdress")
        message, address = self.sock.recvfrom(1024)
        data = message.decode("utf-8")
        self.dict_miners = data
        print("словарь майнеров ",self.dict_miners)
    
    def SendRequestToSetMode(self, mode):
        if mode == 1:
            self.SendRequest(self.ip_miner, self.info_main_miner_port, b"RequestToSetMode1")
        if mode == 2:
            self.SendRequest(self.ip_miner, self.info_main_miner_port, b"RequestToSetMode2")



user = Listener()

user.SendRequestToGetMainMiners()
user.SendRequestToGetMainPort()
user.SendRequestToGetListenersAdress()
user.SendRequestToGetMinersAdress()
user.SendRequestToSetMode(1)

