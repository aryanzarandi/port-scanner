import socket
import os
print("In Memories Of All Rained Flower")
print("Hi This is Port Scanner Written by Aryan")
print("To Use it Enter IP or HostName and First and Last Port Number To Scan ")
print("Also You Can See Result in Result.txt File ") 
#function to Check port is open or not
def check(host, port):
    
    s = socket.socket()
    try:
        
        s.connect((host, port))
       
    except:
        
        return False
    else:
       
        return True
       
host = input("Enter the host address or IP :")#catch host add from User
response = os.system("ping -c 1 " + host)#try to ping host
 
if response == 0:
  startport=input("Enter First port to scan ")
  try:
   startport=int(startport)
   endport=input("Enter Last port ")
  except:
   print("not an integer")
  try:
    endport=int(endport)
    if startport>endport:#check first por number less than second port number
        print("Not acceptable Value")
    else:
        try:
            f=open("Result.txt","w+")#open file
            f.write("The host is %s  \n----------------------------\n" % host)
        except:
            print("Cannot Open The File")
        for port in range(int(startport), int(endport)):#check port
            if check(host, port):
                print(" The port Number  ", port," is Open ")
                f.write("The port Number %d is opened\n" % port)
            else:
                print(" The port Number  ", port," is Blocked ")
                f.write("The port Number %d is closed\n" % port)
    f.close()      
  except:
    print("not an integer")
 
else:
    print(host," Not reachable")
