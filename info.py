import requests 
import json
from rich import print as rich_print

def get_user_info(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        if user_data:
            return user_data
        else:
            print(f"There is no user {username} in github!") 
            return []  
    else:
        print(f"Faild , faild code: {response.status_code}")
        return []

def print_events(events , username):
    rich_print(f"Latest events for [bold green]{username}[/bold green]:")
    for event in events:
            if event['type'] == 'IssueCommentEvent':
                rich_print(f"- commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
                rich_print(f"- pushed to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                rich_print(f"- created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                rich_print(f"- starred {event['repo']['name']}")
            elif event['type'] == 'PullRequestEvent':
                rich_print(f"- created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewEvent':
                rich_print(f"- reviewed pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                rich_print(f"- commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'CreateEvent':
                rich_print(f"- created {event['payload']['ref_type']} {event['payload']['ref']}")
            else:
                rich_print(f"- {event['type']}")
                                                   

