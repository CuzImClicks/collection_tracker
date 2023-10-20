
import time
import requests

api_key = "30a14cfc-6ec1-476b-b470-dd5d509cd656"

while True:

    players = [line.split(" ") for line in open("players.txt", "r").read().split("\n")]
    # read the players and generate a list containing 
    # smaller lists containing the name and uuid (just like a csv)
    # we read the file, split it on every new line and then
    # split each line on each space
    # we can use the [x for x in list] syntax

    content = ""

    for player in players:
        # get active profile
        profile_data = requests.get(f"https://api.hypixel.net/skyblock/profile?key={api_key}&profile={player[2]}").json()
        # get collection
        if not "collection" in profile_data["profile"]["members"][player[1]]:
            print(f"{player[0]} has collection api off")
            continue
        gold_ingot = profile_data["profile"]["members"][player[1]]["collection"]["GOLD_INGOT"]
        line = f"{player[0]} {player[1]} {player[2]} {gold_ingot}\n"
        print(line, end="")
        content += line
        # we then add to the content variable
        # each line contains one player, the profile played on and the collection they had
    
    print("Done!")
    # we then save all of the data in a file with the current time
    with open(f"data/{round(time.time())}.txt", "w+") as f:
        f.write(content)

    time.sleep(60 * 3)