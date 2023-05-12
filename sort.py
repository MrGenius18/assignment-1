import csv

with open("users.csv", mode="r") as file:
    reader = csv.DictReader(file)
    sorted_users = sorted(reader, key=lambda user: user["FirstName"])

with open("users-sorted.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "FirstName", "LastName", "Username", "Email", "Avatar", "Gender", "DoB", "Address"])
    writer.writeheader()
    writer.writerows(sorted_users)