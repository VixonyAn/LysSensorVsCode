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

while True:
    msg, addr = socket_reciever.recvfrom(3000)
    msg_str = msg.decode()
    print(f"UDP Broadcaster {addr} sent the following message: {msg_str}")
    msg_obj = json.loads(msg_str)
    try:
        response = requests.post(REST_API_URL, json=msg_obj, verify=False, timeout=5)
        print(f"Response from REST API: {response.status_code} -- {response.text}")
    except requests.exceptions.RequestException as error:
        print(f"Error occured when posting to REST API: {error}")
