from socket import *
from threading import *
from random import *


def switch_case(sentence):
    match sentence:
        case "random":
            connectionSocket.send("Input two numbers seperated by *space*".encode())
            input = connectionSocket.recv(1024).decode()
            numbers = input.split()
            if len(numbers) != 2:
                connectionSocket.send("Invalid input. Please enter two numbers separated by a space.".encode())
                return
            try:
                num1, num2 = map(int, numbers)
                #Range bliver plusset med en.
                random_num = randint(min(num1, num2), max(num1, num2)+1)
                response = f"{random_num}"
                connectionSocket.send(response.encode())
            except ValueError:
                connectionSocket.send("Invalid input. Please enter two valid numbers.".encode())
        case "add":
            connectionSocket.send("Input two numbers seperated by *space*".encode())
            input = connectionSocket.recv(1024).decode()
            numbers = input.split()
            if len(numbers) != 2:
                connectionSocket.send("Invalid input. Please enter two numbers separated by a space.".encode())
                return
            try:
                num1, num2 = map(int, numbers)
                add_num = num1 + num2
                response = f"{add_num}"
                connectionSocket.send(response.encode())
            except ValueError:
                connectionSocket.send("Invalid input. Please enter two valid numbers.".encode())
        case "subtract":
            connectionSocket.send("Input two numbers seperated by *space*".encode())
            input = connectionSocket.recv(1024).decode()
            numbers = input.split()
            if len(numbers) != 2:
                connectionSocket.send("Invalid input. Please enter two numbers separated by a space.".encode())
                return
            try:
                num1, num2 = map(int, numbers)
                sub_num = (num1) - (num2)
                response = f"{sub_num}"
                connectionSocket.send(response.encode())
            except ValueError:
                connectionSocket.send("Invalid input. Please enter two valid numbers.".encode())
       
def handleClient(connectionSocket, address):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        sentence = sentence.lower().strip()
        switch_case(sentence)        


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target = handleClient,args = (connectionSocket, addr)).start()

    