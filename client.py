import cloudpickle

# 求和函数
def my_sum(l):
    return sum(l)

# 序列化
seri_func = cloudpickle.dumps(my_sum)

# RPC
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8011))
s.send(seri_func)
result = s.recv(1024)
print(result.decode('utf-8'))
s.close()