import subprocess

def ping_ip(ip_address):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False
    
    In [7]: %time ping_ip('google.com')
CPU times: user 0 ns, sys: 4 ms, total: 4 ms
Wall time: 2.03 s
Out[7]: True
In [8]: %time ping_ip('8.8.8')
CPU times: user 0 ns, sys: 8 ms, total: 8 ms
Wall time: 12 s
Out[8]: False
In [9]: items = [1, 3, 5, 7, 9, 1, 2, 3, 55, 77, 33]
In [10]: %time sorted(items)
CPU times: user 0 ns, sys: 0 ns, total: 0 ns
Wall time: 8.11 μs
Out[10]: [1, 1, 2, 3, 3, 5, 7, 9, 33, 55, 77]