
import socket
import time
import os

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False

def connectToServer(hostName, port):
    try:
        clientSocket.connect((socket.gethostname(), 65535))
        print(f"Connected to {hostName}:{port} successfully")

        toggleConnected()
        os.system('cls||clear')
    except Exception as exception:
        print(f"Error occurred whilst attempting to connect to server")
        print("\n")
        print(f"{exception}")

def toggleConnected():
    global connected
    connected = not connected

def sendToServer(message):
    clientSocket.send(bytes(message, "utf-8"))

print("Welcome to the UNO Client!")
print("Please start by entering the host name and port")
print("\n")

port = int(input("Port: "))
host_name = input("Host Name: ")

print("\n")
print("Attempting Connection to server")
time.sleep(1)

connectToServer(socket.gethostname(), port)

while True:
    client_input = input("> ")
    sendToServer(client_input)

