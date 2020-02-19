import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = 'data.pr4e.org'

def scanner(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if scanner(x):
        print('port',x,' is open!!!!!!')
    else:
        print('port',x,' is closed')
        
    
'''
We can scan through 65000 ports,
but obviously this is not an efficient port scanner.
So generally what people do is they will thread the port scanner.
'''
