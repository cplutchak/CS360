import socket
import time
import random

quotes = [
    "In running, it doesn’t matter whether you come in first, in the middle of the pack, or last. You can say, ‘I have finished.’ There is a lot of satisfaction in that.",
    "Running is the greatest metaphor for life, because you get out of it what you put into it.",
    "The miracle isn’t that I finished. The miracle is that I had the courage to start.",
    "Run when you can, walk if you have to, crawl if you must, just never give up.",
    "Run often. Run long. But never outrun your joy of running.",
    "Strength does not come from physical capacity. It comes from an indomitable will.",
]

def get_motivational_quote(mile_goal):
    # Select a random quote
    quote = random.choice(quotes)
    return f"Mile Achievement: {mile_goal}\nMotivation: {quote}"

def main():
    # Create a socket object
    srvr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine name and set port
    host = socket.gethostname()
    port = 2024

    # Bind to the port
    srvr_socket.bind((host, port))

    # Now wait for client connection.
    srvr_socket.listen(5)

    print("Waiting for Mile Goal Achieved..")

    while True:
        # Establish connection with client.
        client_socket, addr = srvr_socket.accept()
        print('Connection Secured...', addr)

        # Receive mile goal from client
        mile_goal = float(client_socket.recv(1024).decode())

        if mile_goal in [5, 10, 13.1, 26.2]:
            # Get a motivational quote
            quote = get_motivational_quote(mile_goal)
            print('Retrieving Motivation...')
            time.sleep(1)
            print(f". . .")
            time.sleep(1)

            # Get a motivational quote based on the mile goal
            quote = get_motivational_quote(mile_goal)
            print('Motivation Retrieved...')
            time.sleep(1)
            print(f". . .")
            time.sleep(1)

            # Send the motivational quote back to the client
            client_socket.send(quote.encode())
            print('Motivation Sent...')
            client_socket.send(quote.encode())
        else:
            client_socket.send("Mile goal not supported".encode())

        # Close the connection with the client
        client_socket.close()

if __name__ == "__main__":
    main()