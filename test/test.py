import base64
import json
import sys
from datetime import datetime
import requests as r


def test_fastapi():
    iterations = 1000

    with open("black.png", "rb") as image_file:
        img = image_file.read()
        img = base64.b64encode(img)

    fast_api = send_request(iterations, img, 8000)
    flask_api = send_request(iterations, img, 5000)
    print("fastapi speed >>> ", fast_api)
    print("flask speed >>> ", flask_api)


def send_request(iterations, encoded_string_img, port):
    payload = {"count": iterations, "payload": []}
    for i in range(iterations):
        payload["payload"].append(
            {
                "arbitrary_field": f"{i}",
                "image": encoded_string_img.decode("utf-8"),
            }
        )

    print(sys.getsizeof(json.dumps(payload)))
    x = datetime.utcnow()
    request = r.post(url=f"http://127.0.0.1:{port}/test", json=payload)
    y = datetime.utcnow() - x
    print(request.content)
    return y


