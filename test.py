from app import get_origin_ip, send_request_with_custom_body, get_my_public_ip
import json

def test_ip_origin():

    assert get_my_public_ip() == get_origin_ip()

def test_json_body_response():

    body =   {
        "name":"Linna Azaiez",
        "group": "RT5/2"
    }

    response_json = send_request_with_custom_body(body=body)

    data = json.loads(response_json.get("data"))

    for key in body.keys():
        assert key in data.keys()
        assert body.get(key) == data.get(key)

    assert len(data.keys()) == len(body.keys())