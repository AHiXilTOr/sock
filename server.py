import threading, socket

LOCALHOST = '127.0.0.1'
PORT = 1488

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((LOCALHOST, PORT))
print('Сервер запущен...')

class ClientThread(threading.Thread):
    def __init__(self, clientaddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.caddres = clientaddress
        print('Подключился: ', clientaddress)

    def run(self):
        msg = ''
        while True:
            try:
              data = self.csocket.recv(4096)
              msg = data.decode()
              print(msg)
              if msg ==  '':
                  break
              elif msg == 'сервер':
                  self.csocket.send(bytes('работает', 'UTF-8'))
            except ConnectionResetError:
              print('Отключился:' + self.caddres)
              return
            
while True:
    server.listen(1)
    clientsock, clientaddress = server.accept()
    newthread = ClientThread(clientaddress, clientsock)
    newthread.start()