import socket
import threading as thread
import json
import gameplay



sub1 = json.dumps({
    "request": "subscribe",
    "port": 8888,
    "name": "OmegaZero",
    "matricules": ["18198,20286"]
    })


pong = json.dumps({"response": "pong"})



def subs():
    b=0
    addr = ("172.17.10.40", 3000)
    with socket.socket() as s:
        s.connect(addr)
        s.send(sub1.encode())

        s.close()
   

def mess1():
    print("ok")
    c=0
    addr2 = ("0.0.0.0", 8888)
    with socket.socket() as so:
        
        so.bind(addr2)
        so.listen()
        print("i listen")
        while True:
            client, address = so.accept()
            
            with client:
                mess = client.recv(2048).decode()
                message=json.loads(mess)
                
                
                if message["request"] == "ping":
                    client.send(pong.encode())
                    
                    
                        
                if "state" in message:
                    gameplay.Info(message,client)
                    
                    
                




if __name__ == "__main__":
        print (__name__)
        subs()
        mess1()
        
        
        
        
        
