from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket
import os

# Generate a pair of RSA keys
keys = RSA.generate(2048)
public_key = keys.publickey()

# Create a cipher object
cipher = PKCS1_OAEP.new(public_key)

# The message to be sent
message = "Hi-World"

# Encrypt the message
encrypted_message = cipher.encrypt(message.encode())

# Create a socket object
s = socket.socket()

# Get local machine name
host = socket.gethostname()

# Randomize the port number
port = os.urandom(2)

# Connect to the server
s.connect((host, port))

# Send the encrypted message
s.send(encrypted_message)

# Close the connection
s.close()
