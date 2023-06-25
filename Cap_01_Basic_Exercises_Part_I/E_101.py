
# The program acesses and prints a URL content to the console

#Method 01
from http.client import HTTPConnection

con =HTTPConnection("github.com")
con.request("GET", "/")

result = con.getresponse()
content = result.read()

print(content)

#Method 02
import requests

data = requests.get("https://github.com/marsabatini")
print(data.text)