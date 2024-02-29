from socket import *

def send_command(command, serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(command.encode())
    response = clientSocket.recv(1024).decode()
    print('From Server:', response)
    return clientSocket

def send_numbers(numbers, clientSocket):
    clientSocket.send(numbers.encode())
    response = clientSocket.recv(1024).decode()
    print('From Server:', response)
    clientSocket.close()

serverName = 'localhost'
serverPort = 12000

command = input("Enter command (random, add, subtract): ")
clientSocket = send_command(command, serverName, serverPort)

numbers = input("Enter two numbers separated by space: ")
send_numbers(numbers, clientSocket)