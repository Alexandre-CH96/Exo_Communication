import network

IP = "10.0.0.124"
PORT = 1120

while True: 
    socket = network.newClientSocket()
    socket.connect((IP,PORT))

    print("Tape la lettre a afficher")
    lettre = input(">>> ")
    
    socket.send(lettre.encode())
    