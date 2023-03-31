import socket
import time
import wikipy
from os import system

system("clear")
BUFFER = 32768
x = 1
while (x):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svr_add = ('localhost', 8000)
        sock.connect(svr_add)
    
        keySearch= input("Search: ")
        if (not(wikipy.search_list(keySearch))):
            continue

        keyIndex = int(input("Enter: "))
        SearchKey = ','.join(str(x) for x in (keySearch, keyIndex))
        sock.sendall(SearchKey.encode())
        print()
        print("Sent request!!")
        print()

        srch_data = sock.recv(BUFFER).decode()

        if (srch_data.endswith('L')):

            srch_data = srch_data.rstrip(srch_data[-1])
            li = list(srch_data.split(";"))

            print("There is a disambiguation.", end = ' ')
            print(keySearch, "may refer to:")
            for i in range(1,len(li)):
                print(str(i) + ") " + li[i])

            keyIndex = int(input("Enter: "))
            SearchKey = li[keyIndex]
            sock.sendall(SearchKey.encode())
            print()
            print("Sent request!!")
            print()
            print()
            print()

            srch_data = sock.recv(BUFFER).decode()

            print(srch_data)
            print("received")

            x = -1
            while(x != 0 and x != 1):
                print("Do you want to continue? (1 for YES and 0 for NO): ", end = '')
                try:
                    x = int(input())
                except:
                    print("Invalid Input. Please try again.")
                    continue
            if (not(x)):
                break
            if (x):
                continue

        print()
        print()

        print(srch_data)
        print()
        print()
        print("Received!!\n\n")

        x = -1
        while(x != 0 and x != 1):
            print("Do you want to continue? (1 for YES and 0 for NO): ", end = '')
            try:
                x = int(input())
            except:
                print("Invalid Input. Please try again.")
                print()
                continue
            if (x != 0 and x != 1):
                print("Invalid choice. Please try again")
            print()
    

        if (not(x)):
            break
    except (ConnectionRefusedError, ConnectionResetError, ConnectionError):
        print("Server not active or refused to connect. Please try again maybe after some time")
        exit(1)

sock.close()
