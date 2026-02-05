import requests 
import json

def get_user_info(username):
    url = f"https://api.github.com/users/{user_name}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
       user_data = response.json()
       print(json.dumps(user_data, indent=4, ensure_ascii=False))
    else:
        print(f"Faild , faild code: {response.status_code}")

user_name = input("Enter a username which you want to know: ")
get_user_info(user_name)