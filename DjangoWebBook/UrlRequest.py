from urllib import request

url = 'http://www.rebalance.co.kr'
f = request.urlopen(url)
print(f.read())