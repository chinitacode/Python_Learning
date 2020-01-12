# Objective
The chatroom program aims to achieve the following features: 
1. Allow multiple persons to access the chat room and communicate with each other; 
2. Each time when a client program is run, on the screen of the server the connection information should be displayed
indicating the rank of the client(ordered by the time of connection), its IP address and the port connected; 
3. On entering the chat room, the user should enter his/her username so as each time when the user sends a message, the message got displayed
on the screen of others with that user name to indicate the source of the information; 
4. The user can enter 'exit' to leave the chat room, and all other users got notified by the message 'User {user_name} left the chat room'
and then this client's socket got closed, but the other users can still communicate with each other normally; 
5. The server itself can shut down the chat room, kicking all users off from it by entering 'exit' in its window,
and all the users got notified by the message 'Chat room closing...press ENTER to exit', and then users all press ENTER to leave.


# Technical Design 
The server uses a thread **transmit** to forward all messages sent by clients, and the client uses a thread **rec** to receive messages.
To close the socket connection, the server also uses a thread **exit** to detect whether 'exit' has been entered in the server's window.
Once the server actively disconnects the socket connection, all clients got notified immediately and then will be forced to close its socket connection. 

# Caveats 
For now on the part of clients, all the functionalities are achieved successfully, whereas on the part of server, errors occurrs
when server tries to close all sockets entering 'exit' in its window.
