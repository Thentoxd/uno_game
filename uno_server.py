import socket
import threading

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 65535
max_players = 2
players = []
openSocket = True


def startSocket():
    main_socket.bind((socket.gethostname(), port))
    main_socket.listen(max_players)

    print(f"Running Uno Server on {socket.gethostname()}:{port}")
    print(f"Max Players: {max_players}")
    print("\n")
    print("Console:")

    while openSocket:
        clientSocket, address = main_socket.accept()

        player = UnoPlayer(clientSocket, address)
        print("Testing 'openSocket'")
        players.append(player)

        thread = threading.Thread(target=handle_client, args=(player, address, clientSocket))
        thread.start()

    close_server()


def close_server():
    print("TEST CLOSE_SERVER")

    main_socket.close()
    exit()


def handle_client(player, address, connection):
    print(f"Connection from {address} has been established!")

    connected = True
    while connected:
        message = connection.recv(1024).decode("utf-8")
        print("Testing 'connected'")

        if message == "!disconnect":
            connected = False

            print(f"[{player.name}: {address}] has disconnected")
            break

        if message.startswith("!"):
            player.handle_command(message)

            print(f"[{player.name}: {address}] send a command: '{message}'")
        elif message.startswith("INFO"):
            args = message.split(" ")

            player.setName(args[1])
        else:
            print(f"[{player.name}: {address}] send a message: '{message}'")

    connection.close()


def broadcast(message):
    print("TEST BROAD COMMAND")

    for i in range(0, len(players)):
        players[i].sendMessage(message)


def invalid_command(command, message):
    print(f"Invalid use of command: '{command}'")
    print(f"{message}")


def handle_command(command_string):
    args = command_string.split(" ")
    print(args)
    print("TEST HANDLE COMMAND")

    if args[0] == "!stop":
        if args[1] == None:
            openSocket = False
        else:
            invalid_command(args[0], "Please confirm the stop command with '!stop confirm'")
    elif args[0] == "!broad":
        broadcast(args[1])


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

    def handle_command(self, command_string):
        args = command_string.split(" ")
        if args[0] == "!NAME":
            self.setName(args[1])


startSocket()

while True:
    command_input = input("> ")
    if command_input != "" and command_input.startswith("!"):
        handle_command(command_input)
