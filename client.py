import threading, socket, sys

SERVER = '127.0.0.1'
PORT = 1488

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def task1():
    while True: 
        in_data = client.recv(4096)
        print('От сервера: ' + in_data.decode())

def task2():
    while True: 
        out_data = input()
        client.sendall(bytes(out_data, 'UTF-8'))

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()