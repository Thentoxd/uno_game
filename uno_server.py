
import socket
import threading

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

        thread = threading.Thread(target=handle_client, args=(clientSocket, address))
        thread.start()

        command_input = input("> ")


def handle_client(connection, address):
    print(f"Connection from {address} has been established!")
    player = UnoPlayer(connection, address)
    players.append(player)

    connected = True
    while connected:
        message = connection.recv(1024).decode("utf-8")
        if message == "!DISCONNECT":
            connected = False

            print(f"[{player.name}: {address}] has disconnected")
            break

        if message.startswith("!"):
            handle_command(player, message)

            print(f"[{player.name}: {address}] send a command: '{message}'")
        else:
            print(f"[{player.name}: {address}] send a message: '{message}'")

    connection.close()

def handle_command(player, command_string):
    args = command_string.split(" ")
    if args[0] == "!NAME":
        player.setName(args[1])

def broadCast(message):
    for i in range(0, len(players)):
        players[i].sendMessage(message)

class CommandExecutor:
    def __init__(self, executor_priority):
        self.executor_priority = executor_priority

class UnoPlayer(CommandExecutor):
    def __init__(self, socket, address):
        super().__init__("PLAYER")
        self.clientSocket = socket
        self.address = address
        self.name = str(address)

    def sendMessage(self, message):
        self.clientSocket.send(bytes(message, "utf-8"))

    def setName(self, name):
        self.name = name



startSocket()
