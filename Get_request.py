#sending Get request to a domain and fetching a data in specific format

import http.client

connection = http.client.HTTPSConnection("www.journaldev.com")

connection.request("GET", "/")

response = connection.getresponse()


print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()



