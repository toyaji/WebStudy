from urllib import parse

# url 을 파싱해서 반환
url = 'https://www.google.co.kr/webhp;paul?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=xampp+%EC%95%84%ED%8C%8C%EC%B9%98&*'
result = parse.urlparse(url)
print(result)