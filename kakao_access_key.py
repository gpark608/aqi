import requests
import os
from dotenv import load_dotenv

load_dotenv()


KAKAO_REFRESH_TOKEN = os.getenv('KAKAO_REFRESH_TOKEN')
KAKAO_REST_API_KEY = os.getenv('KAKAO_REST_API_KEY')
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "refresh_token",
    "client_id": KAKAO_REST_API_KEY,
    "refresh_token": KAKAO_REFRESH_TOKEN
}
response = requests.post(url, data=data)
tokens = response.json()

print(tokens)