import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    if (
        allowed
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context


allowSelfSignedHttps(True)
data = {
    "input_data": {
        "columns": [
            "budget_usd",
            "employees_impacted",
            "duration_months",
            "risk_level",
            "risk_numeric",
        ],
        "index": [0],
        "data": [[50000, 10, 12, "Medium", 3]],
    }
}


body = str.encode(json.dumps(data))

url = "https://roi-vukzq.eastus2.inference.ml.azure.com/score"
api_key = "3nvSjEQDZMGcSJpBP56wflOFX4yJ5E2XtuO8hYIClh5PaZamMnbPJQQJ99BCAAAAAAAAAAAAINFRAZML4Zli"
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": ("Bearer " + api_key),
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    print(error.info())
    print(error.read().decode("utf8", "ignore"))
