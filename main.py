sock = socket(
    AF_INET,
    SOCK_STREAM | SOCK_NONBLOCK)

# Bind the socket to the internet with a port number
sock.bind(("::", 32007))
