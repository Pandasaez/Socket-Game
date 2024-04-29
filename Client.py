import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 9999))

while True:
    # Get user input
    guess = input("Enter your guess: ")

    # Send the guess to the server
    client_socket.send(guess.encode())

    # Receive and display server's response
    response = client_socket.recv(1024).decode()
    print(response)

    if response == "correct":
        break

# Close the connection
client_socket.close()
