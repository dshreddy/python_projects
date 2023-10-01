import requests
from datetime import datetime

# https://pixe.la/

# create a user account
api = "https://pixe.la/v1/users"
parameters = {
    "token": "cehbebfeqhbfhkerfljeqfh",
    "username": "dshr",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=api, json=parameters)
# print(response.text)



# Create a graph
graph_api = "https://pixe.la/v1/users/dshr/graphs"
head_parameter = {
    "X-USER-TOKEN": "cehbebfeqhbfhkerfljeqfh"
}
graph_config_parameters = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "momiji",
}
# response = requests.post(url=graph_api, json=graph_config_parameters, headers=head_parameter)
# print(response.text)



# Post a pixel
pixel_api = "https://pixe.la/v1/users/dshr/graphs/graph1"
today = datetime.now().strftime("%Y%m%d")

pixel_parameters = {
    "date": today,
    "quantity": "5"
}
# response = requests.post(url=pixel_api, headers=head_parameter, json=pixel_parameters)
# print(response.text)



# Update a pixel
date_to_change = "20230423"
update_api = f"https://pixe.la/v1/users/dshr/graphs/graph1/{date_to_change}"
update_parameters = {
    "quantity": "3"
}
# response = requests.put(url=update_api, headers=head_parameter, json=update_parameters)
# print(response.text)



# Delete a pixel
date_to_delete = "20230423"
delete_api = f"https://pixe.la/v1/users/dshr/graphs/graph1/{date_to_delete}"
# response = requests.delete(url=delete_api, headers=head_parameter)
# print(response.text)

