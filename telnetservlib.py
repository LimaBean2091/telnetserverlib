import socket
1
class TelnetServer():
    host = None
    port = None
    telSock = None
    connection = None
    addr = None
    
    def __init__(self,host='127.0.0.1',port=23):
        self.host = host;
        self.port = port;
        self.bind_socket()
        
    def bind_socket(self):
        self.telSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.telSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.telSock.bind((self.host,self.port))
        self.telSock.listen()
        
    def waitForConnection(self):
        self.connection, self.addr = self.telSock.accept()
        
    def write(self,message):
        if (self.connection is not None and message is not None):
            self.connection.sendall(bytearray(message,'UTF-8'))
            
    def writeln(self,message):
        if (self.connection is not None and message is not None):
            self.connection.sendall(bytearray(message+"\n",'UTF-8'))

    def read_until(self,bytecount=1024):
        if (self.connection is not None):
            commands = self.connection.recv(26)
            data = self.connection.recv(bytecount);
            try:
                return data.decode('UTF-8'), commands.decode('UTF-8')
            except:
                return None
        
    def query(self,query):
        if (self.connection is not None and query is not None):
            self.write(query)
            data = b''
            commands = self.connection.recv(26);
            while True:
                chunk = self.connection.recv(1)
                if (chunk == b'\r'):
                    break
                data += chunk.replace(b'\x05',b'');
            try:
                return data.decode('UTF-8'), commands
            except:
                return None,None
    
    def getIP(self):
        if (self.addr is not None):
            return self.addr[0]
        else:
            return "NO CONNECTION";
    
    def getPort(self):
        if (self.addr is not None):    
            return self.addr[1]
        else:
            return "NO CONNECTION";
    
    def dropConnection(self):
        if (self.connection is not None):
            self.connection.close()
            self.connection = None;
            self.addr = None;