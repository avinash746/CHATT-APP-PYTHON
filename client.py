# from socket import AF_INET, socket, SOCK_STREAM
# from threading import Thread
# import tkinter


# def receive():
#     while True:
#         try:
#             msg = client_socket.recv(BUFSIZ).decode("utf8")
#             msg_list.insert(tkinter.END, msg)
#         except OSError:
#             break


# def send(event=None):
#     msg = my_msg.get()
#     my_msg.set("")
#     client_socket.send(bytes(msg, "utf8"))
#     if msg == "{quit}":
#         client_socket.close()
#         top.quit()


# def on_closing(event=None):
#     my_msg.set("{quit}")
#     send()


# top = tkinter.Tk()
# top.title("Chat Box")

# messages_frame = tkinter.Frame(top)
# my_msg = tkinter.StringVar()
# my_msg.set("Type your messages here.")
# scrollbar = tkinter.Scrollbar(messages_frame)
# msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# msg_list.pack()
# messages_frame.pack()

# entry_field = tkinter.Entry(top, textvariable=my_msg)
# entry_field.bind("<Return>", send)
# entry_field.pack()
# send_button = tkinter.Button(top, text="Send", command=send)
# send_button.pack()

# top.protocol("WM_DELETE_WINDOW", on_closing)


# HOST = input('Enter host: ')
# PORT = input('Enter port: ')
# if not PORT:
#     PORT = 33000
# else:
#     PORT = int(PORT)

# BUFSIZ = 1024
# ADDR = (HOST, PORT)

# client_socket = socket(AF_INET, SOCK_STREAM)
# client_socket.connect(ADDR)

# receive_thread = Thread(target=receive)
# receive_thread.start()


# # Start the GUI execution
# tkinter.mainloop()

# from socket import AF_INET, socket, SOCK_STREAM
# from threading import Thread
# import tkinter


# def receive():
#     """Handles receiving messages from the server."""
#     while True:
#         try:
#             msg = client_socket.recv(BUFSIZ).decode("utf8")
#             msg_list.insert(tkinter.END, msg)
#         except OSError:  # Handles errors, such as when the client exits
#             break


# def send(event=None):
#     """Handles sending messages to the server."""
#     msg = my_msg.get()
#     my_msg.set("")  # Clears the input field
#     client_socket.send(bytes(msg, "utf8"))
#     if msg == "{quit}":
#         client_socket.close()
#         top.quit()


# def on_closing(event=None):
#     """Handles closing the window."""
#     my_msg.set("{quit}")
#     send()


# # GUI Setup
# top = tkinter.Tk()
# top.title("Chat Box")

# # Frame to display messages
# messages_frame = tkinter.Frame(top)
# my_msg = tkinter.StringVar()  # For the message to be sent
# my_msg.set("Type your messages here.")
# scrollbar = tkinter.Scrollbar(messages_frame)  # For scrolling messages
# msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# msg_list.pack()
# messages_frame.pack()

# # Entry field for typing messages
# entry_field = tkinter.Entry(top, textvariable=my_msg)
# entry_field.bind("<Return>", send)  # Press Enter to send a message
# entry_field.pack()

# # Button to send messages
# send_button = tkinter.Button(top, text="Send", command=send)
# send_button.pack()

# # Handle window closing
# top.protocol("WM_DELETE_WINDOW", on_closing)

# # Socket Setup
# while True:
#     try:
#         HOST = input('Enter host: ')
#         PORT = input('Enter port: ')
#         try:
#             PORT = int(PORT) if PORT else 33000
#             if not (0 <= PORT <= 65535):
#                 raise ValueError("Port number must be between 0 and 65535.")
#         except ValueError as e:
#             print(f"Invalid port: {e}")
#             continue  # Prompt again if the port is invalid

#         BUFSIZ = 1024
#         ADDR = (HOST, PORT)

#         client_socket = socket(AF_INET, SOCK_STREAM)
#         client_socket.connect(ADDR)
#         break  # Exit loop when successfully connected
#     except Exception as e:
#         print(f"Error connecting to the server: {e}. Please try again.")

# # Start receiving messages in a separate thread
# receive_thread = Thread(target=receive)
# receive_thread.start()

# # Start the GUI execution
# tkinter.mainloop()

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Handles receiving messages from the server."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            # Socket is closed or another error occurred
            break


def send(event=None):
    """Handles sending messages to the server."""
    if not client_socket:
        msg_list.insert(tkinter.END, "Error: Not connected to the server.")
        return
    try:
        msg = my_msg.get()
        my_msg.set("")  # Clears the input field
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()
    except OSError as e:
        msg_list.insert(tkinter.END, f"Error sending message: {e}")


def on_closing(event=None):
    """Handles closing the window."""
    my_msg.set("{quit}")
    send()


# GUI Setup
top = tkinter.Tk()
top.title("Chat Box")

# Frame to display messages
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the message to be sent
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # For scrolling messages
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

# Entry field for typing messages
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)  # Press Enter to send a message
entry_field.pack()

# Button to send messages
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

# Handle window closing
top.protocol("WM_DELETE_WINDOW", on_closing)

# Socket Setup
client_socket = None
while True:
    try:
        HOST = input("Enter host : ")
        PORT = input("Enter port: ")
        PORT = int(PORT) if PORT else 33000
        if not (0 <= PORT <= 65535):
            raise ValueError("Port number must be between 0 and 65535.")

        BUFSIZ = 1024
        ADDR = (HOST, PORT)

        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(ADDR)
        print(f"Connected to server at {ADDR}.")
        break
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"Error connecting to the server: {e}. Please try again.")

# Start receiving messages in a separate thread if connected
if client_socket:
    receive_thread = Thread(target=receive)
    receive_thread.start()
    # Start the GUI execution
    tkinter.mainloop()
