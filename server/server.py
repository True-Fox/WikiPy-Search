import socket
import wikipy
import wikipedia
from os import system

system("clear")
BUFFER = 32768

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
svr_add = ('',8000)
sock.bind(svr_add)

sock.listen(9)
print("Server listening on", svr_add)

while True:

    conn, cli_add = sock.accept()
    print("Connection from", cli_add)
    
    data = conn.recv(BUFFER).decode()
    
    print("Keyword: " + data +" received")
    
    keyword, index = tuple(data.split(","))

    summary, x = wikipy.search_wiki(keyword,index)

    if x:
        summary = summary + 'L'
        conn.sendall(summary.encode())

        data = conn.recv(BUFFER).decode()
        print("Keyword: " + data +" received")
        keyword = data
        print(keyword)

        summary = wikipedia.summary(keyword)
        conn.sendall(summary.encode())
        print("------------------------------------------")

        conn.close()
        continue

    conn.sendall(summary.encode())
    
    print("------------------------------------------")
    conn.close()

sock.close()
