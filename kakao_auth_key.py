import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()
KAKAO_REST_API_KEY = os.getenv('KAKAO_REST_API_KEY')
REDIRECT_URI = "http://localhost/oauth"

KAKAO_AUTH_URI = f"https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"

def login_handler():
    webbrowser.open(KAKAO_AUTH_URI)

login_handler()