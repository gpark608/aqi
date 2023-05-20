import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
AQI_TOKEN = os.getenv('AQI_TOKEN')
KAKAO_TOKEN = os.getenv('KAKAO_TOKEN')
def lookup_aqius(aqius_value):
    # range look-up:
    for (start, end), aqius in aqius_range.items():
        if start <= aqius_value <= end:
            return aqius

    return "Unknown"


aqius_range = {
    (0,50): ['Good','Air quality is satisfactory, and air pollution poses little or no risk.'],
    (51,100): ['Moderate','Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'],
    (101,150): ['Unhealthy for Sensitive Groups','Members of sensitive groups may experience health effects. The general public is less likely to be affected.'],
    (151,200): ['Unhealthy','Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'],
    (201,300): ['Very Unhealthy','Health alert: The risk of health effects is increased for everyone.'],
    (301,1000): ['Hazardous','Health warning of emergency conditions: everyone is more likely to be affected.']
}

aqi_url = 'http://api.airvisual.com/v2/city'
aqi_params = {
    'city': 'Calgary',
    'state': 'Alberta',
    'country': 'Canada',
    'key': AQI_TOKEN
}

aqi_response = requests.get(aqi_url, params=aqi_params)
aqi_data = aqi_response.json()

AQI_LEVEL=lookup_aqius(aqi_data['data']['current']['pollution']['aqius'])[0]
AQI_DESC=lookup_aqius(aqi_data['data']['current']['pollution']['aqius'])[1]

url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Bearer {KAKAO_TOKEN}'
}
template_object={
        "object_type": "text",
        "text": f"AQI_LEVEL: {AQI_LEVEL}\n{AQI_DESC}",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
data = {
        "template_object": json.dumps(template_object)
    }


response = requests.post(url, headers=headers, data=data)
print(response)



