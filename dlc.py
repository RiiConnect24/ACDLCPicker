import acwc24
import calendar
import os
import pickle
import random
import requests
import subprocess
from datetime import datetime

items = ["anniversary_cake",
         "blue_Pikmin_hat",
         "bus_model",
         "Chihuahua_model",
         "dachshund_model",
         "dalmatian_model",
         "Dolphin_model",
         "Eiffel_tower",
         "fedora_chair",
         "flamenco_hat",
         "GameCube_dresser",
         "Gracie_dresser",
         "green_headgear",
         "guard_s_helmet",
         "hopscotch_floor",
         "Kapp_n_model",
         "Labrador_model",
         "ladder_shades",
         "Nintendo_DS_Lite",
         "Nintendo_DSi_B",
         "Nintendo_DSi_W",
         "Pave_clock",
         "red_Pikmin_hat",
         "shopping_cart",
         "sweets_player",
         "tam_o_shanter",
         "Wii_locker",
         "wildflower_floor",
         "yellow_Pikmin_hat"]
#        "creepy_bat_stone",
#        "creepy_carpet",
#        "creepy_cauldron",
#        "creepy_clock",
#        "creepy_coffin",
#        "creepy_crystal",
#        "creepy_skeleton",
#        "creepy_statue",
#        "creepy_stone",
#        "creepy_wallpaper",
#        "election_poster",
#        "golden_bed",
#        "golden_bench",
#        "golden_carpet",
#        "golden_chair",
#        "golden_clock",
#        "golden_closet",
#        "golden_dresser",
#        "golden_man",
#        "golden_screen",
#        "golden_table",
#        "golden_wallpaper",
#        "golden_woman",
#        "Mushroom_rack"]


items_seasonal = {}

items_seasonal[1] = ["snowman_head", "snowman_vanity"]
items_seasonal[2] = ["Cupid_bench"]
items_seasonal[3] = ["egg_TV", "shamrock_hat"]
items_seasonal[4] = ["egg_TV"]
items_seasonal[5] = []
items_seasonal[6] = ["banana_split_hat", "hot_dog_hat", "sand_castle"]
items_seasonal[7] = ["banana_split_hat", "hot_dog_hat", "sand_castle"]
items_seasonal[8] = ["banana_split_hat", "hot_dog_hat", "sand_castle"]
items_seasonal[9] = ["pile_of_leaves"]
items_seasonal[10] = ["pile_of_leaves"]
items_seasonal[11] = ["pile_of_leaves"]
items_seasonal[12] = ["snowman_head", "snowman_vanity", "Jingle_TV", "festive_wreath"]

def picker():
    month = datetime.today().month
    items_all = items + items_seasonal[month]
    choice = random.choices(items_all, weights=[1] * len(items) + [2] * len(items_seasonal[month]), k=1)[0]
    return choice

if os.path.exists("dlc.pickle"):
    dlc_list = pickle.load(open("dlc.pickle", "rb"))
    choice = list(dlc_list.values())[-1]
    while choice in list(dlc_list.values())[:len(items)]:
        choice = picker()
    dlc_id = list(dlc_list.keys())[-1] + 1
else:
    dlc_list = {}
    choice = picker()
    dlc_id = 1
    
print("The next DLC item will be: " + choice + "!")
    
dlc_list[dlc_id] = choice
pickle.dump(dlc_list, open("dlc.pickle", "wb"))
acwc24.create(choice, False, 8192 + dlc_id)

region2 = {}

region2["E"] = "us"
region2["P"] = "eu"
region2["J"] = "jp"
region2["K"] = "kr"

for region in ["E", "P", "J", "K"]:
    subprocess.call(["mv", "build/" + choice + "_" + region + ".arc.wc24", "/var/www/wapp.wii.com/nwcs/public_html/ruu/rvforestdl_" + region2[region] + ".enc"])

dlc_message = "We are now distributing this item:\n\n" + choice + "\n\nEnjoy!"

data = {"username": "Animal Crossing DLC Bot", "content": dlc_message,
        "avatar_url": "http://rc24.xyz/images/logo-small.png", "attachments": [
            {"fallback": dlc_message, "color": "#549537", "author_name": "RiiConnect24 Animal Crossing DLC Script",
                "author_icon": "https://rc24.xyz/images/webhooks/animalcrossing/pete.png",
                "text": dlc_message, "title": "Update!",
                "fields": [{"title": "Script", "value": "Animal Crossing Wii", "short": "false"}],
                "footer": "RiiConnect24 Script",
                "footer_icon": "https://rc24.xyz/images/logo-small.png",
                "ts": int(calendar.timegm(datetime.utcnow().timetuple()))}]}

webhook_url = open("webhook_url.txt", "rb").read()

post_webhook = requests.post(webhook_url.replace(b"\n", b""), json=data, allow_redirects=True)
