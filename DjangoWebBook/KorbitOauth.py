import oauth2
import requests
from requests import auth

#코빗 토큰 얻기 - 다이렉트 인증으로 바이 안에다가 유저명이랑 비번 다 집어넣음


client_id = 'wvOfwR3yvlw5WvAn74ro1pRWStb8HT3450NprLlUe1PTYl1ZccoPUtSlxwRGe'
client_secret = 'Dqt8gWcJd1eCtVfotr8Z5EXC0nowmFVbs9vWwrmhsM1A8lrzeXDfvEior1OcV'
username = 'happytoday83@naver.com'
password = 'qkdnf87!'


def get_token():
    post_data = {
        "client_id": client_id,
        "client_secret":client_secret,
        "username": username,
        "password": password,
        'grant_type': 'password'
    }

    respon = requests.post('https://api.korbit.co.kr/v1/oauth2/access_token', data=post_data)
    print(respon)
    tokendata = respon.json()
    print(tokendata)
    return tokendata

def get_userinfo(tokendata):
    token = tokendata['access_token']
    post_data = 'Authorization: Bearer ' + token
    respon = requests.get('https://api.korbit.co.kr/v1/user/info', data=post_data)
    print(respon)
    info = respon.json()
    print(info)



if __name__ == '__main__':
    tokendata = get_token()
    get_userinfo(tokendata)