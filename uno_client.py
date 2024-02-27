
import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectToServer(hostName, port):
    try:
        main_socket.connect((socket.gethostname(), 65535))
        print(f"Connected to {hostName}:{port} successfully")
    except Exception as exception:
        print(f"Error occurred whilst attempting to connect to server")
        print("\n")
        print(f"{exception}")

def recieveMessage():
    message = main_socket.recv(1024)

    return message.decode("utf-8")

print("Welcome to the UNO Client!")
print("Please start by entering the host name and port")
print("\n")

port = int(input("Port: "))
host_name = input("Host Name: ")

print("\n")
time.sleep(1)
print("Attempting Connection to server")
time.sleep(1)

connectToServer(socket.gethostname(), port)

while True:
    print(recieveMessage())
