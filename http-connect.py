import http.client

connection = http.client.HTTPConnection('www.domain.xyz', 80, timeout=10)

print(connection)

#simple script to connect to specific domain name and port in python
