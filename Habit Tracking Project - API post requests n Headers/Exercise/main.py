import requests
from datetime import datetime

USERNAME = "ruuu"
TOKEN = "qwertyuiop12345"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# use to create user account using this
# after creating, we can comment out the lines of codes
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Gym",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# To create the graph, once created, we can comment out
# response = requests.post(url = graph_endpoint, json=graph_parameters, headers = headers)
# print(response.text)

post_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now
DATE = today.strftime("%Y%m%d")

post_a_pixel_parameters = {
    "date": DATE,
    "quantity": "1",
}
# response = requests.post(post_a_pixel_endpoint, json=post_a_pixel_parameters, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
update_pixel_parameters = {
    "quantity": "2",
}
# update a pixel
# response = requests.put(update_pixel_endpoint,json=update_pixel_parameters,headers=headers )
# print(response.text)

# delete pixel
delete_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
response = requests.delete(delete_a_pixel_endpoint, headers=headers)
print(response.text)