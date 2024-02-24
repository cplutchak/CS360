# CS361
CS361 Individual & Partner Project

# CS361 Partner Microservice (Mile Goal Motivation)
This microservice utilizes sockets to provide a motivational quote once a running mile goal has been met by the user of the application.

# Utilizing the Microservice
1. A connection is first established between the client and the server, host = localhost & port = 2024.
2. The user then enters the mile goal that was achieved, options are 5, 10, 13.1, or 26.2.
   a. If one of those options is not chosen, the user is prompted to enter one of the correct options.
3. Once a valid input is received it is sent to the server to be recieved and return appropriate response.
4. With the valid input received the server goes through three steps:
   a. Retrieving Motivation (2 seconds)
   b. Motivation Retrieved (2 seconds)
   c. Motivation Sent
5. The random quote is sent back to the client and then printed.
6. The user is then again prompted to enter a new valid input.
