from urllib import request

# HTTP 기본 인증 요청을 위한 핸들러 생성
auth_handler = request.HTTPBasicAuthHandler()
auth_handler.add_password(realm=None, uri='https://api.korbit.co.kr/v1/oauth2/access_token', user='toyaji', passwd='qkdnf87!')

opner = request.build_opener(auth_handler)


# 디폴트 오프너로 설정하면 urlopen 으로 함수 요청 가능
request.install_opener(opner)
u = request.urlopen('https://api.korbit.co.kr/v1/oauth2/access_token')