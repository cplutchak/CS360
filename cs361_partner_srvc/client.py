import socket

def main():
    while True:
        # Get the mile goal from the user
        mile_goal = float(input("Enter your mile goal achieved: "))

        if mile_goal not in [5, 10, 13.1, 26.2]:
            print("Unsupported mile goal. Please enter 5, 10, 13.1, or 26.2.")
            continue

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Get the local machine name and set port
            host = socket.gethostname()
            port = 2024

            # Connect to the server
            client_socket.connect((host, port))

            # Send the mile goal to the server
            client_socket.send(str(mile_goal).encode())

            # Receive the motivational quote from the server
            quote = client_socket.recv(1024).decode()

            # Print the motivational quote
            print(quote)
        finally:
            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    main()