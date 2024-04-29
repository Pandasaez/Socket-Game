import socket
import threading
import random

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific port
server_socket.bind(('localhost', 9999))

# Listen for incoming connections
server_socket.listen(2)
print("Waiting for connections...")

# Generate a random number for clients to guess
number_to_guess = random.randint(1, 100)
print(f"Number to guess: {number_to_guess}")

# Function to handle each client's connection
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}.")

    while True:
        # Receive guess from client
        guess = client_socket.recv(1024).decode()

        if not guess:
            break

        # Check if the guess is correct
        guess = int(guess)
        if guess == number_to_guess:
            client_socket.send("correct".encode())
            break
        elif guess < number_to_guess:
            client_socket.send("higher".encode())
        else:
            client_socket.send("lower".encode())

    # Close the connection
    client_socket.close()

# Accept and handle connections from clients
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
