import requests 

username = input("Enter your username: ")

url = f"https://www.tiktok.com/@{username}"

response = requests.get(url)

if response.status_code == 200:
    print(f"User '{username}' exists on TikTok.")
else:
    print(f"User '{username}' does not exist on TikTok.")