import requests
import csv
import time

def get_random_user():
    response = requests.get("https://random-data-api.com/api/users/random_user")
    if response.status_code ==200:
        return response.json()
    else:
        return None

with open("users.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "FirstName", "LastName", "Username", "Email", "Avatar", "Gender", "DoB", "Address"])
    while True:
        user = get_random_user()
        if user:
            writer.writerow([user["id"], user["first_name"], user["last_name"], user["username"], user["email"], user["avatar"], user["gender"], user["date_of_birth"], user["address"]])
        time.sleep(1)
