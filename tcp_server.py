import socket
import sys

#creating the TCP/IP socket
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#designating server ip
print("Please input the IP to listen on(default localhost)")
servip = input("")

#designating the port
print("Please input port to listen (1500 - 65000")
servport = int(input(""))
if servport < 1500 or servport > 65000:
    servport = 31337

#setting the server address
servaddr = (servip, servport)
print("Starting server on " + str(servip) + ":" + str(servport))
servsock.bind(servaddr)

#Listen for receiving data
servsock.listen(1)

#wait for connection
while True: #accept connections from these addresses
    #this can be used to whitelist connections
    connection, clientaddr = servsock.accept()

#when a connection arrives
    try:
        print("incoming connection from " + str(clientaddr))

#recieving the data in chunks
        while True:
            recv = "".encode() #blank declaration
            recv = recv + connection.recv(1024) #making our full message
            #(just incase over 1024 bytes)
            received = recv.decode()#decode the message into a usable variable            
            print("Incoming: " + str(received)) #print the incoming request

            #what to do with recieved
            if len(received) > 1:
                #picking up what the servers puttin down
                receivedlist = received.split(" ")

                def CostFinder(location,adults,childs):
                    adultcost = int(0)#blankdeclaration
                    childcost = int(0)#blankdeclaration
                    if location == "Stockholm":
                        adultcost = int(adults) * 100#number of adults * ticket price
                        childcost = int(childs) * 60#number of children * ticket price
                    elif location == "Rome":
                        adultcost = int(adults) * 400
                        childcost = int(childs) * 220      
                    elif location == "Jamaica":
                        adultcost = int(adults) * 1100
                        childcost = int(childs) * 850
                    elif location == "Hamburg":
                        adultcost = int(adults) * 800
                        childcost = int(childs) * 650
                    elif location == "Copenhagen":
                        adultcost = int(adults) * 2800
                        childcost = int(childs) * 2200
                    elif location == "Kiel":
                        adultcost = int(adults) * 2500
                        childcost = int(childs) * 2000
                    else:
                        print("read location error")
                    totalcost = adultcost + childcost #work out the total cost
                    return(totalcost)#return the totalcost

                lengthoflist = len(receivedlist) #taking how many arguments we have
                inputscount = int(lengthoflist)#putting it in a usable int
                count=0#set the count to 0
                for i in range(0,int(inputscount/4)):#range of amount of sets of 4 inputted
                    cabinno = receivedlist[0+count]#cabin number found
                    #print(str(cabinno))
                    location = receivedlist[1+count] #location found
                    #print(str(location))
                    #running our function to find the cost
                    cost = CostFinder(location,receivedlist[2+count],receivedlist[3+count])
                    #print(cost)
                    response = str(cabinno) + ", Your Excursion to " +\
                               str(location)+ " would cost £" + str(cost)
                    #responding to the client

                    print(str(response))
                    if count >= lengthoflist:#if the count is past our amount of inputs
                        connection.close()#stop sending
                        print("Finished connection with " + str(clientaddr))
                        break
                    print("Sending:")
                    connection.sendall(response.encode())#if not, send our response
                    count+=4#add to our count
                

            else: #if received < 1
                break

    finally: #close the connection
        connection.close()

        
