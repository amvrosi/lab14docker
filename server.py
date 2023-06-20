import socket
from datetime import datetime

# konfiguracja portu
PORT = 8888

# imię i nazwisko autora
AUTHOR = "Ivan Sobol"

# utworzenie gniazda sieciowego (socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# przypisanie adresu IP i portu do gniazda sieciowego
server_socket.bind(('0.0.0.0', PORT))

# wyświetlenie informacji o uruchomieniu serwera
print(f'Server started on port {PORT}, author: {AUTHOR}, at: {datetime.now()}')

# oczekiwanie na połączenie klienta
server_socket.listen(1)

# utworzenie pliku z logami
with open('logs.txt', 'w') as logs_file:
    # zapisanie informacji o uruchomieniu serwera do logów
    logs_file.write(f'Server started on port {PORT} by {AUTHOR} at {datetime.now()}\n')

    # obsługa połączenia z klientem
while True:
    # akceptowanie połączenia z klientem
    client_socket, client_address = server_socket.accept()

    # wyświetlenie informacji o połączeniu
    print(f'Connection from {client_address}')

    # odczyt adresu IP klienta
    client_ip = client_address[0]

    # pobranie aktualnej daty i godziny
    now = datetime.now()

    # wyświetlenie informacji na serwerze
    print(f'Client IP: {client_ip}')
    print(f'Date and time in client timezone: {now}')

    # utworzenie strony HTML z informacjami dla klienta
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Client information</title>
        </head>
        <body>
            <h1>Client information:</h1>
            <p>IP address: {client_ip}</p>
            <p>Date and time in your timezone: {now}</p>
        </body>
    </html>
    """

    # wysłanie strony HTML do klienta
    client_socket.sendall(f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n{html}'.encode())

    # zamknięcie połączenia z klientem
    client_socket.close()