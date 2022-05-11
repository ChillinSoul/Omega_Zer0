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


pong = json.dumps({"response": "pong"})



def subs():
    b=0
    addr = ("127.0.0.1", 3000)
    with socket.socket() as s:
        s.connect(addr)
        s.send(sub1.encode())

        s.close()
   

def mess1():
    print("ok")
    c=0
    addr2 = ("127.0.0.1", 8888)
    with socket.socket() as so:
        
        so.bind(addr2)
        so.listen()
        print("i listen")
        while True:
            client, address = so.accept()
            print("accepted")
            with client:
                mess = client.recv(2048).decode()
                message=json.loads(mess)
                
                
                if message["request"] == "ping":
                    client.send(pong.encode())
                    
                    print("Youpi! Il est là!")
                        
                if "state" in message:
                    gameplay.Info(message,client)
                    
                    
                




if __name__ == "__main__":
        print (__name__)
        subs()
        mess1()
        
        
        
        
        