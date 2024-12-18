# from socket import AF_INET, socket, SOCK_STREAM
# from threading import Thread


# def accept_incoming_connections():
#     while True:
#         client, client_address = SERVER.accept()
#         print("%s:%s has connected." % client_address)
#         client.send(bytes("Hello user!! Type your name and press enter!", "utf8"))
#         addresses[client] = client_address
#         Thread(target=handle_client, args=(client,)).start()


# def handle_client(client):
#     name = client.recv(BUFSIZ).decode("utf8")
#     welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
#     client.send(bytes(welcome, "utf8"))
#     msg = "%s has joined the chat!" % name
#     broadcast(bytes(msg, "utf8"))
#     clients[client] = name

#     while True:
#         msg = client.recv(BUFSIZ)
#         if msg != bytes("{quit}", "utf8"):
#             broadcast(msg, name+": ")
#         else:
#             client.send(bytes("{quit}", "utf8"))
#             client.close()
#             del clients[client]
#             broadcast(bytes("%s has left the chat." % name, "utf8"))
#             break


# def broadcast(msg, prefix=""):
#     for sock in clients:
#         sock.send(bytes(prefix, "utf8")+msg)

        
# clients = {}
# addresses = {}

# HOST = ''
# PORT = 33000
# BUFSIZ = 1024
# ADDR = (HOST, PORT)

# SERVER = socket(AF_INET, SOCK_STREAM)
# SERVER.bind(ADDR)

# if __name__ == "__main__":
#     SERVER.listen(5)
#     print("Waiting for connection...")
#     ACCEPT_THREAD = Thread(target=accept_incoming_connections)
#     ACCEPT_THREAD.start()
#     ACCEPT_THREAD.join()
#     SERVER.close()

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Handles incoming connections."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Hello user!! Type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    """Broadcasts a message to all clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

# Use '127.0.0.1' for local testing
HOST = '127.0.0.1'  
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
