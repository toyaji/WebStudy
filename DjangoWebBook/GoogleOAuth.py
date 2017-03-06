# 구글에 OAuth2를 이용해서 로그인하고 사용자 정보를 가져오는
# 샘플 코드

import requests
import json
from pprint import pprint
from urllib.parse import urlencode
from subprocess import Popen

# Auth2 인증 정보가 들어 있는 파일에서 데이터를 읽는다.
# 이런 파일이다.
#
# 이 파일은
#    https://console.developers.google.com
# 에서 앱을 만들고 credential을 생성한다.
#
# {
#   "installed": {
#     "redirect_uris": [
#       "urn:ietf:wg:oauth:2.0:oob",
#       "http:\/\/localhost"
#     ],
#     "client_secret": "xxx",
#     "auth_provider_x509_cert_url": "https:\/\/www.googleapis.com\/oauth2\/v1\/certs",
#     "token_uri": "https:\/\/accounts.google.com\/o\/oauth2\/token",
#     "auth_uri": "https:\/\/accounts.google.com\/o\/oauth2\/auth",
#     "project_id": "xxx",
#     "client_id": "xxx"
#   }
# }
with open('crediential_secrets2.json') as f:
    credentials = json.load(f)
    credentials = credentials["installed"]

client_id = credentials['client_id']
client_secret = credentials['client_secret']
redirect_uri = credentials['redirect_uris'][0]
auth_uri = credentials['auth_uri']
token_uri = credentials['token_uri']

def retrieve_authorization_code():
    """
    인증 API를 이용해서 authorization_code를 받는다.
    """

    auth_code_req = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": ("https://www.googleapis.com/auth/userinfo.profile")
    }

    # 인증 요청 주소 확인
    # 사용자 인증을 위한 URL이 반환된다. 사용자가 직접 확인해야 하기 때문에
    # redirect를 하지 않았다.
    r = requests.get("{}?{}".format(auth_uri, urlencode(auth_code_req)),
                     allow_redirects=False)
    url = r.headers.get('location')

    # 웹브라우져가 열리고 화면에 로그인을 하면 code를 받을 수 있다.
    # 아래는 맥의 경우

    # 혹시 웹브라우저가 실행되지 않으면 URL: 에 나오는 URL를 브라우저이
    # 직접 입력한다.
    print("URL: " + url)
    Popen(["open", url])

    # 웹 화면에서 확인한 Code를 입력한다.
    authorization_code = input("\nAuthorization Code >>> ")
    return authorization_code

def retrieve_tokens(auth_code):
    """
    access_token, refresh_token을 받아 온다.
    """
    # access token 요청을 위한 데이터
    access_token_req = {
        "code" : auth_code,
        "client_id" : client_id,
        "client_secret" : client_secret,
        "redirect_uri" : redirect_uri,
        "grant_type": "authorization_code",
    }
    content_length=len(urlencode(access_token_req))
    access_token_req['content-length'] = str(content_length)

    # 요청
    r = requests.post(token_uri, data=access_token_req)
    data = r.json()
    # data에 access_token 정보가 들어있다.
    return data

"""
Sample code of fetching user information from userinfo API.
"""
def get_userinfo(access_token):
    """
    userinfo API로 데이터를 받아온다.
    """

    # access_token을 header에 붙여서 요청한다.
    header = {"Authorization": "OAuth %s" % access_token}
    r = requests.get("https://www.googleapis.com/oauth2/v2/userinfo",
                     headers=header)
    data = r.json()
    return data

def main():
    token = retrieve_authorization_code()
    print('authorization code : ' + token)
    access_token = retrieve_tokens(token)
    print('access_token data:')
    pprint(access_token)
    data = get_userinfo(access_token["access_token"])
    print('data:')
    pprint(data)

if __name__ == '__main__':
    main()