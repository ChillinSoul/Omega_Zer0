import socket
import threading as thread
import json
import gameplay



sub1 = json.dumps({
    "request": "subscribe",
    "port": 8888,
    "name": "OmegaZero",
    "matricules": ["18192,20281"]
    })

sub2 = json.dumps({
    "request": "subscribe",
    "port": 8881,
    "name": "OmegaZero1",
    "matricules": ["18198,20286"]
    })


pong = json.dumps({"response": "pong"})



def subs(sub):
    b=0
    addr = ("127.0.0.1", 3000)
    with socket.socket() as s:
        s.connect(addr)
        s.send(sub.encode())

        s.close()
   
addr1 = ("127.0.0.1", 8888)
addr2 = ("127.0.0.1", 8881)
def mess(adr):
    print("ok")
    c=0
    
    with socket.socket() as so:
        
        so.bind(adr)
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
        subs(sub1)
        mess(addr1)
        
        
        
        
        
