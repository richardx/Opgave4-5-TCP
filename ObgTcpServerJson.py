from socket import *
from threading import *
from random import *
import json

def switch_case(data, connectionSocket):
    # metoden bliver lavet om til lower case
    method = data.get("method", "").lower()
    
    if method == "random":
        # henter num1 og num2 fra data 
        num1 = data.get("num1")
        num2 = data.get("num2")
        # laver en variabel, som genererer et tilfældigt tal mellem num1 og num2 ved hjælp af randint
        random_num = randint(min(num1, num2), max(num1, num2))
        response = {"Random number between first and second number": random_num}
        # sender response til clienten

    elif method == "add":
        # henter num1 og num2 fra data
        num1 = data.get("num1")
        num2 = data.get("num2")
        # laver en variabel, som lægger num1 og num2 sammen
        add_num = num1 + num2
        response = {"first + second number": add_num}
        # sender response til clienten
        
    elif method == "subtract":
        # henter num1 og num2 fra data
        num1 = data.get("num1")
        num2 = data.get("num2")
        # laver en variabel, som trækker num2 fra num1
        sub_num = num1 - num2
        response = {"first - second number": sub_num}
        # sender response til clienten

    else:
        response = {"error": "Invalid method"}
    # sender response til clienten
    connectionSocket.send(json.dumps(response).encode())

def handleClient(connectionSocket, address):
    # laver en while loop, som kører så længe der er en forbindelse
    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        try:
            data = json.loads(data)
            switch_case(data, connectionSocket)
        except json.JSONDecodeError:
            # hvis der er en fejl i JSON, så sendes der en fejl til clienten
            connectionSocket.send(json.dumps({"error": "Invalid JSON"}).encode())

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
