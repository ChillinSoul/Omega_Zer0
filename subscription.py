import socket
import threading as thread
import json
import gameplay


sub1 = json.dumps({
    "request": "subscribe",
    "port": 8888,
    "name": "Patate",
    "matricules": ["64187"]
    })
sub2 =json.dumps({
        "request": "subscribe",
        "port": 6666,
        "name": "Cornichon",
        "matricules": ["56411"]
 })

pong = json.dumps({"response": "pong"})



def subs():
    b=0
    addr = ("127.0.0.1", 3000)
    with socket.socket() as s:
        s.connect(addr)
        s.send(sub1.encode())

        s.close()
    with socket.socket() as s:
        s.connect(addr)
        s.send(sub2.encode())
        s.close()

def mess1():
    c=0
    addr2 = ("127.0.0.1", 8888)
    with socket.socket() as so:
        so.bind(addr2)
        so.listen()
        while True:
            client, address = so.accept()
            with client:
                mess = client.recv(2048).decode()
                message=json.loads(mess)
                
                if message["request"] == "ping":
                    client.send(pong.encode())
                    while c<1:
                        print("Youpi! Il est là!")
                        c=1
                if "state" in message:
                    gameplay.Info(message,client)
                client.close()

def mess2():
    c=0
    addr3 = ("127.0.0.1", 6666)
    with socket.socket() as so:
        so.bind(addr3)
        so.listen()
        while True:
            client, address = so.accept()
            with client:
                mess = client.recv(2048).decode()
                message=json.loads(mess)
                
                if message["request"]=="ping":
                    client.send(pong.encode())
                    while c<1:
                        print("Youpi! Il est là!")
                        c=1
                if "state" in message:
                    gameplay.Info(message,client)
                
                client.close()



if __name__ == "__main__":
        print (__name__)
        subs()
        thread1 = thread.Thread(target=mess1, daemon=True)
        thread1.start()
        mess2()
        