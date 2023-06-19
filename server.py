from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket
import os

# Generate a pair of RSA keys
keys = RSA.generate(2048)
public_key = keys.publickey()

# Create a cipher object
cipher = PKCS1_OAEP.new(public_key)

# Create a socket object
s = socket.socket()

# Get local machine name
host = socket.gethostname()

# Randomize the port number
port = os.urandom(2)

# Bind to the port
s.bind((host, port))

# Start listening for connections
s.listen(5)

while True:
    # Accept a connection
    c, addr = s.accept()
    
    # Receive the message
    encrypted_message = c.recv(1024)

    # Decrypt the message
    message = cipher.decrypt(encrypted_message)

    # Print the message
    print(message.decode())

    # Close the connection
    c.close()
