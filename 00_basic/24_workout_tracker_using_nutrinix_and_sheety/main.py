import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

# https://developer.nutritionix.com/admin/applications/1409623356141
# https://dashboard.sheety.co/projects/64468d8ce848b542a0a0bf7d/sheets/workouts

GENDER = "male"
WEIGHT_KG = "64"
HEIGHT_CM = "170"
AGE = "19"

APP_ID = "f012c245"
API_KEY = "c35c7340365d3e827d356c1290a9a02a"
nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "00"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
post_row_endpoint = f"https://api.sheety.co/6e74bff51888a5891a571d54a9761508/workoutTracking/workouts"
get_endpoint = "https://api.sheety.co/6e74bff51888a5891a571d54a9761508/workoutTracking/workouts"
row_to_delete = 2
delete_row_endpoint = f"https://api.sheety.co/6e74bff51888a5891a571d54a9761508/workoutTracking/workouts/{row_to_delete}"


exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=nutritionix_header)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    basic = HTTPBasicAuth('dshr', 'Dshreddy03@')
    sheet_response = requests.post(url=post_row_endpoint, json=sheet_inputs, auth=basic)
    # bearer = {
    #     "Authorization": "Bearer token"
    # }
    # sheet_response = requests.post(url=post_row_endpoint, json=sheet_inputs, auth=bearer)
    print(sheet_response.text)




