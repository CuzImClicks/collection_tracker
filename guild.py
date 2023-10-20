import requests

api_key = "30a14cfc-6ec1-476b-b470-dd5d509cd656"

guild = requests.get(f"https://api.hypixel.net/guild?key={api_key}&name=Mining Cult").json()

players = []

def get_active_profile(uuid):
    profile_data = requests.get(f"https://api.hypixel.net/skyblock/profiles?key={api_key}&uuid={uuid}").json()
    if profile_data["profiles"] is None:
        return ""
    for profile in profile_data["profiles"]:
        if profile["selected"]:
            return profile["profile_id"]

content = ""

for member in guild["guild"]["members"]:
    res = requests.get(f"https://api.minetools.eu/uuid/{member['uuid']}").json()
    line = f"{res['name']} {res['id']} {get_active_profile(res['id'])}\n"
    print(line)
    content += line

with open("players.txt", "w+") as f:
    f.write(content)