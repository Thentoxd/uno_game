import socket
import time
import os

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = "Alex"
connected = False


def connectToServer(hostName, port):
    try:
        clientSocket.connect((socket.gethostname(), 65535))
        print(f"Connected to {hostName}:{port} successfully")

        toggleConnected()
        os.system('cls||clear')
        sendToServer(f"INFO {name}")

    except Exception as exception:
        print(f"Error occurred whilst attempting to connect to server")
        print("\n")
        print(f"{exception}")


def toggleConnected():
    global connected
    connected = not connected


def update_name(newName):
    name = newName
    print(f"Updated name to '{name}'")


def sendToServer(message):
    clientSocket.send(bytes(message, "utf-8"))


print("Welcome to the UNO Client!")

while True:
    client_input = input("> ")
    args = client_input.split(" ")

    if connected:
        message = clientSocket.recv(1024).decode("utf-8")

        if message != "":
            print(message)

    if args[0] == "!connect":
        server = args[1].split(":")
        host = server[0]
        port = int(server[1])

        print("\n")
        print("Attempting connection to server.")
        time.sleep(1)

        connectToServer(socket.gethostname(), port)
    elif args[0] == "!name":
        if len(args) <= 1:
            print(f"Name: '{name}'")
        else:
            update_name(args[1])
    else:
        sendToServer(client_input)

