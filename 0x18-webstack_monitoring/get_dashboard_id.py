import requests
import json

# Datadog API credentials
API_KEY = '6dfaf10bee4c611d13b50eb5e2b3098e'
APP_KEY = '249058576b53ff57f9a5b3c71864f269175092a1'

# Function to fetch dashboard ID
def get_dashboard_id(api_key, app_key, dashboard_name):
    url = f"https://api.datadoghq.com/api/v1/dashboard"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    dashboards = response.json()['dashboards']
    for dashboard in dashboards:
        if dashboard['title'] == dashboard_name:
            return dashboard['id']
    return None

# Replace 'your_dashboard_name' with the name of your dashboard
dashboard_name = 'Youssef\'s Dashboard Thu, Apr 11, 6:24:39 am'

# Get dashboard ID
dashboard_id = get_dashboard_id(API_KEY, APP_KEY, dashboard_name)

# Write dashboard ID to file
with open('2-setup_datadog', 'w') as f:
    f.write(str(dashboard_id))
