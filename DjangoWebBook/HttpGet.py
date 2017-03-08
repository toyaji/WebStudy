from urllib.request import urlopen

# get 방식
url = 'http://www.example.com'
f = urlopen(url)
print(f.read(500))

# post 방식
data = b"query=python"
p = urlopen(url, data)
print(p.read(500))