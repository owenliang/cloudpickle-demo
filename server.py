import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8011))
s.listen(5)

while True:
    sock, _ = s.accept()
    seri_func = sock.recv(1024)
    import pickle
    my_sum = pickle.loads(seri_func)
    result = my_sum(list(range(1,100)))
    sock.send(str(result).encode('utf-8'))
    sock.close()