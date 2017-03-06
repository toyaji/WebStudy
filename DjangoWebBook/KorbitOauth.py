import oauth2
import requests
from requests import auth

#코빗 토큰 얻기 - 다이렉트 인증으로 바이 안에다가 유저명이랑 비번 다 집어넣음


client_id = 'toyaji'
client_secret = 'qkdnf87!'
username = 'toyaji'
password = 'qkdnf87!'


def get_token():
    post_data = {
        "client_id": client_id,
        "client_secret":client_secret,
        "username": username,
        "password":password
    }

    respon = requests.post('https://api.korbit.co.kr/v1/oauth2/access_token', data=post_data)
    tokendata = respon.json()
    print(tokendata)

if __name__ == '__main__':
    get_token()