import requests, os, time
from dotenv import load_dotenv, set_key
      
def initToken():
    load_dotenv()
    url = "https://www.onemap.gov.sg/api/auth/post/getToken"
        
    payload = {
            "email": os.environ['ONEMAP_EMAIL'],
            "password": os.environ['ONEMAP_EMAIL_PASSWORD']
        }

    response = requests.request("POST", url, json=payload)
    response = response.json()
    token = response["access_token"]

    # Setting new API key in .env session (HOTFIX)
    os.environ["ONEMAP_API_KEY"] = token
    time.sleep(1)

    if os.environ["ONEMAP_API_KEY"]:
        return True
    
    return False

def getResponse(url):
    load_dotenv()
    api_key = os.environ["ONEMAP_API_KEY"]
    headers = {"Authorization": api_key}
    
    res = requests.request("GET", url, headers=headers).json()
    return res