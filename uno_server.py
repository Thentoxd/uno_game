
import socket

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 65535
max_players = 2
players = []

def startSocket():
    main_socket.bind((socket.gethostname(), port))
    main_socket.listen(max_players)

    print(f"Running Uno Server on {socket.gethostname()}:{port}")
    print(f"Max Players: {max_players}")
    print("\n")
    print("Console:")

    while True:
        clientSocket, address = main_socket.accept()
        print(f"Connection from {address} has been established!")

        player = UnoPlayer(socket=clientSocket, address=address)
        player.sendMessage("YOY")

        players.append(player)


class UnoPlayer:
    def __init__(self, socket, address):
        self.clientSocket = socket
        self.address = address

    def sendMessage(self, message):
        main_socket.send(bytes(message, "utf-8"))


startSocket()

