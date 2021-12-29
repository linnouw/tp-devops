import requests

BASE_URL = "https://httpbin.org/"

def get_my_public_ip():

    return requests.get('https://checkip.amazonaws.com').text.strip()


def get_origin_ip():

    URL = BASE_URL + "ip"

    response = requests.get(url=URL)

    return response.json().get("origin")

def send_request_with_custom_body(body: dict):
    URL = BASE_URL + "post"

    response = requests.post(url=URL, json=body)

    return response.json()


if __name__ == "__main__":

    print(f"Hello. My ip is {get_my_public_ip()}")
