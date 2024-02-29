import requests


def modify():
    url = "http://127.0.0.1:8000/api/modify/3/"
    payload = 'name=ESP8266&descriptions=%D0%A1%D0%BF%D0%B0%D1%8F%D0%BB_%D1%81%D0%B0%D0%BC'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)


def create():
    url = "http://127.0.0.1:8000/api/get_temp/?name=esp3&descriptions=test3"
    payload = 'name=ESP8266&descriptions=%D0%A1%D0%BF%D0%B0%D1%8F%D0%BB_%D1%81%D0%B0%D0%BC'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def view():
    url = "http://127.0.0.1:8000/api/get_temp/"
    response = requests.request("GET", url)
    print(response.text)

# modify()
# create()
view()