import socket
""" """
import webbrowser

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM

)
""" """

server.bind(
    # socket.gethostbyname_ex("127.0.1.1", 5556)
    ("127.0.0.1", 1234)

)
""" """

server.listen(5)

while True:
    user_socket, adres = server.accept()

    user_socket.send("You are connected".encode("utf-8"))


    # while True:
    #     data = user_socket.recv(1024).decode("utf-8").lower()
    #     print(data)
    #
    #     if data == "youtube":
    #         webbrowser.open('https://www.youtube.com/')
    #
    #     if data == "google":
    #         webbrowser.open('https://www.google.com/')
    #
    #     if data == "vk":
    #         webbrowser.open('https://www.vk.com/')

