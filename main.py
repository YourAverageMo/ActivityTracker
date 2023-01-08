from datetime import datetime

import requests

USERNAME = "mo"
TOKEN = "firsttoken123"
GRAPH_ID = "graph1"

# TODO ____________ CREATE USER ____________
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# TODO ____________ CREAT GRAPH ____________
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint,
#                          json=graph_config,
#                          headers=headers)
# print(response.text)

# TODO ____________ POST PIXEL ____________
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": "20230108",
    "quantity": "25.2",
}
# response = requests.post(url=pixel_endpoint,
#                          json=pixel_config,
#                          headers=headers)
# print(response.text)

# TODO ____________ UPDATE PIXEL ____________
temp_year = "20230107"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{temp_year}"
new_pixel_config = {
    "quantity": "7.8",
}
# response = requests.put(url=update_endpoint,
#                          json=new_pixel_config,
#                          headers=headers)
# print(response.text)

# TODO ____________ DELETE PIXEL ____________
# delete_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{temp_year}"
# response = requests.delete(url=delete_endpoint,
#                          headers=headers)
# print(response.text)
