import csv

def search_user(users, query):
    for user in users:
        if user["id"] == query or user["Username"] == query:
            return user
    return None

with open("users.csv", mode="r") as file:
    reader = csv.DictReader(file)
    users_list = list(reader)

query = input("Enter Id or Username of a user to search: ")
user = search_user(users_list, query)
if user:
    print(f"User Details:\n{user}")
else:
    print("User not found.")