import requests
from bs4 import BeautifulSoup as bs

def log_in_admin():

    client = requests.session()
    LOGIN_URL = 'http://admin.qandi.com/admin'

    site = client.get(LOGIN_URL)

    bs_content = bs(site.content, "html.parser")

    # get the csrf token
    csrf_token = bs_content.find(attrs={"name":"csrf-token"})['content']
    payload = {
        '_token': csrf_token,
        'email': 'temp@thomsondigital.com',
        'passwordenter': '1631689993000',
        'user_type': 1
    }

    response = client.post('https://admin.qandi.com/login',data=payload,cookies=client.cookies)
    print(response)
    return client, csrf_token
    #print(response)