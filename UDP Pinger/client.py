from socket import *
from datetime import datetime
import time
host = "127.0.0.1"
port = 12000

#create a UDP socket
client = socket(AF_INET, SOCK_DGRAM)
# set wait time of 1 sec for timeout
client.settimeout(1)
i = 0

#Ping ten times
for i in range(10):
    sendtime = time.time()
    message = 'Ping' + str(i) + " " + time.ctime(sendtime) #convert index and time to string

    client.sendto((message.encode('utf-8')), (host, port))  #send message
    print("Sent "+ message + "\n")
    
    try:
        data, server = client.recvfrom(4096)
        print("Received " + str(data) + "\n")
        
        receivetime = time.time()
        interval =  receivetime -sendtime
        print("Round Trip Time is " + str(interval*1000) + "\n")
    except timeout:
        print("For " + str(i) + ": Requested timed out")
print("Finished !")
client.close()            
