import socket #the module that we need
import sys

#creating the TCP/IP socket
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#designating server ip
print("Please input the IP you'd like to connect to")
servip = input("")

#designating the port
print("Please input the port to connect to")
servport = int(input(""))

#connecting to the server
servaddr = (servip, servport)
print("Connecting to " + str(servip) + ":" + str(servport))
#connect under the given server address
servsock.connect(servaddr)

try:
    #accepting the clients details
    print("Please input your tickets in this format")
    print("[Cabin No.] [Destination] [No. Adults] [No. Children]")
    print("Example: A22 Stockholm 2 0")
    output = input("")
    print("Sending Request...")
    servsock.sendall(output.encode()) ##sending the client input

    #wait for a response from the server
    #change expected to amount of responses required
    received = 0
    while received == 0: #while nothing is received
        servreceived = "".encode()#blank declaration
        servreceived = servreceived + servsock.recv(1024)
        servresponse = servreceived.decode()#decode the bytes that came in
        print(str(servresponse)) #print the response

finally:
    print("Finished, ending connection")
    servsock.close() #end the connection
