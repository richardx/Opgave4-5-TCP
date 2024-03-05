import json
from socket import *

def send_command(command, serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(command.encode())
    response = clientSocket.recv(1024).decode()
    response_json = json.loads(response)
    print('From Server:', response_json)
    clientSocket.close()
    return response_json

def send_numbers(numbers, clientSocket):
    clientSocket.send(numbers.encode())
    response = clientSocket.recv(1024).decode()
    print('From Server:', response)
    clientSocket.close()

def build_json_request(method, num1, num2):
    # Opretter et JSON-objekt med de angivne parametre
    request = {
        "method": method,
        "num1": num1,
        "num2": num2
    }
    # Returnerer JSON-objektet som string
    return json.dumps(request)

serverName = 'localhost'
serverPort = 12000

command = input("Enter command (random, add, subtract): ")

# Brugerinput til talene
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Opretter JSON-anmodning ved at bruge build_json_request-funktionen
json_request = build_json_request(command, num1, num2)


# Sender JSON-anmodningen til serveren
response_json = send_command(json_request, serverName, serverPort)
