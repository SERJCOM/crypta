import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))

main_adress_miner = {'ip': '127.0.0.1', 'port': 9091}
answer = 0

while True:
    message, address = sock.recvfrom(1024)
    data = message.decode("utf-8")
    print(data)
    if data == "RequestToGetMainMiners":
        answer  = json.dumps(main_adress_miner).encode('utf-8')
        sock.sendto(answer, address)
