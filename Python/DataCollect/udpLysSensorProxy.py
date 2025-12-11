from socket import *
import requests
import json
import urllib3

# In development the ASP.NET Core dev certificate is self-signed.
# Disable warnings and skip verification for local HTTPS calls.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PORT = 32000
socket_reciever = socket(AF_INET, SOCK_DGRAM)
socket_reciever.bind(('', PORT))

print("Proxy UDP ready")
print(f"Listening for incoming messages on PORT {PORT}")

## REST_API_URL = "https://localhost:7169/api/PiData" ## localhost url
REST_API_URL = "https://lysoglivrest.azurewebsites.net/api/PiData" ## Deployed on Azure

PI_DATA = {
    "LightValue" : 0
}

def get_data(response):
    ## print(f"Get Request Successful - {response.status_code}")
    data = response.json()
    return data

def request_delete(id):
    response = requests.delete(f"{REST_API_URL}/{id}")
    if response.status_code == 200:
        print(f"Delete Successful - {response.status_code}: Row {id} Removed")
    elif response.status_code == 404:
        print(f"Delete Failed - {response.status_code}")

while True:
    response_get = requests.get(f"{REST_API_URL}" + "/" + f"{True}", json=PI_DATA)
    if response_get.status_code == 200:
        pi_data = get_data(response_get)
        if len(pi_data) > 10:
            for i in range(len(pi_data) - 1):
                request_delete(pi_data[i]["id"])
    msg, addr = socket_reciever.recvfrom(3000)
    msg_str = msg.decode()
    print(f"UDP Broadcaster {addr} sent the following message: {msg_str}")
    msg_obj = json.loads(msg_str)
    try:
        response = requests.post(REST_API_URL, json=msg_obj, verify=False, timeout=5)
        print(f"Response from REST API: {response.status_code} -- {response.text}")
    except requests.exceptions.RequestException as error:
        print(f"Error occured when posting to REST API: {error}")
