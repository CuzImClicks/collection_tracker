import os
import matplotlib.pylab as plt
import matplotlib.ticker as ticker


def bubblesort(l: list) -> list:
    if len(l) <= 1:
        return l
    
    for i in range(len(l) - 1):
        for j in range(len(l) - i -1):
            swapped = False
            print(int(l[j][3]), int(l[j+1][3]))
            if int(l[j][3]) > int(l[j+1][3]):
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
            if not swapped:
                return l
    return l


def bubblesort_normal(l: list) -> list:
    if len(l) <= 1:
        return l
    
    for i in range(len(l) - 1):
        for j in range(len(l) - i -1):
            swapped = False
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
            if not swapped:
                return l
    return l

def is_sorted(l: list) -> bool:
    for i in range(len(l)-1):
        if int(l[i][-1]) > int(l[i+1][-1]):
            return False
    return True


players = {player.split(" ")[0]: [] for player in open("players.txt").read().split("\n")}

for file in bubblesort_normal([int(x.replace(".txt", "")) for x in os.listdir("data")]):
    values = [player.split(" ") for player in open(f"data/{file}.txt").read().split("\n") if player != ""]
    for value in values:
        players[value[0]].append(value[-1])

players = {p: players[p] for p in players if len(players[p]) != 0 and players[p][0] != players[p][-1]}
start = 1697840433
times = [int(v.replace(".txt", "")) - start for v in os.listdir("data")]
for name in list(players.keys()):
    plt.plot(times, players[name], label=name)
    plt.text(times[-1] + 1, players[name][-1], name, fontsize=10, va="center")

#plt.legend()
plt.savefig("plt.png")