import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

APP_ID = "27cce1ed"
API_KEY = "f0e05e6237a44d051817bdef23d9011d"

nutrient_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/afd19828a0821d28e4e631967a1017e0/workoutTracking/workouts"


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"

}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "age": "30",
    "weight_kg": "6.577"
}

basic = HTTPBasicAuth("mosespeacemccabe", "m@ses23Mc30")

# # make a post request to Nutrient API
response = requests.post(url=nutrient_endpoint, json=parameters, headers=header)
response.raise_for_status()
data = response.json()['exercises']
day = datetime.now()  # return today date
today = day.strftime("%d/%m/%Y")
time_now = day.strftime("%H:%M:%S")
for info in data:
    sheety_parameters = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": f"{info['user_input']}",
            "duration": f"{info['duration_min']}",
            "calories": f"{info['nf_calories']}"
        }
    }

    # make a post request to Sheety to add data to google sheet
    response = requests.post(url=sheety_endpoint, json=sheety_parameters, auth=basic)
    response.raise_for_status()

    print(response.text)
