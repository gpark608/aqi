import requests
import os
from dotenv import load_dotenv

load_dotenv()


KAKAO_REST_API_KEY = os.getenv('KAKAO_REST_API_KEY')
KAKAO_AUTH_CODE = os.getenv('KAKAO_AUTH_CODE')
redirect_uri = 'http://localhost/oauth'
url_token = 'https://kauth.kakao.com/oauth/token'


data = {
    'grant_type':'authorization_code',
    'client_id':KAKAO_REST_API_KEY,
    'redirect_uri':redirect_uri,
    'code': KAKAO_AUTH_CODE,
}

response = requests.post(url_token, data=data)
tokens = response.json()
print("KAKAO_AUTH_CODE="+tokens['refresh_token'])