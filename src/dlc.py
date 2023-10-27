import json

stationery = {
    "anniversary_cake": "bejeweled",
    "banana_split_hat": "cloudy",
    "bus_model": "town_view",
    "Chihuahua_model": "polka_dot",
    "creepy_bat_stone": "halloween",
    "creepy_carpet": "halloween",
    "creepy_cauldron": "halloween",
    "creepy_clock": "halloween",
    "creepy_coffin": "halloween",
    "creepy_crystal": "halloween",
    "creepy_skeleton": "halloween",
    "creepy_statue": "halloween",
    "creepy_stone": "halloween",
    "creepy_wallpaper": "halloween",
    "Cupid_bench": "petal",
    "dachshund_model": "elegant",
    "dalmatian_model": "cow",
    "Dolphin_model": "night_sky",
    "egg_TV": "rainbow",
    "Eiffel_tower": "town_view",
    "election_poster": "lined",
    "fedora_chair": "town_view",
    "festive_wreath": "elegant",
    "flamenco_hat": "buttercup",
    "GameCube_dresser": "tartan",
    "golden_bed": "southwest",
    "golden_bench": "southwest",
    "golden_carpet": "southwest",
    "golden_chair": "southwest",
    "golden_clock": "southwest",
    "golden_closet": "southwest",
    "golden_dresser": "southwest",
    "golden_man": "southwest",
    "golden_screen": "southwest",
    "golden_table": "southwest",
    "golden_wallpaper": "southwest",
    "golden_woman": "southwest",
    "Gracie_dresser": "tartan",
    "green_headgear": "star",
    "guard_s_helmet": "lined",
    "hopscotch_floor": "lined",
    "hot_dog_hat": "hamburger",
    "Jingle_TV": "elegant",
    "Kapp_n_model": "chinese",
    "Labrador_model": "four_leaf",
    "ladder_shades": "buttercup",
    "Mushroom_rack": "forest",
    "Nintendo_DS_Lite": "buttercup",
    "Nintendo_DSi_B": "cool",
    "Nintendo_DSi_W": "cool",
    "Pave_clock": "polka_dot",
    "pile_of_leaves": "maple_leaf",
    "red_Pikmin_hat": "flowery",
    "sand_castle": "cloudy",
    "shamrock_hat": "ribbon",
    "shopping_cart": "ribbon",
    "snowman_head": "snowy",
    "snowman_vanity": "snowman",
    "sweets_player": "lovely",
    "tam_o_shanter": "plaid",
    "Wii_locker": "cool",
    "wildflower_floor": "polka_dot"
}

for k in sorted(stationery.keys()):
    dic = {
        "Regions": ["All"],
        "Unk0": 1,
        "Unk4": 1,
        "LetterId": 0,
        "UnkC": 0,
        "Unk10": 0,
        "ItemFile": f"{k}.bin",
        "DesignFile": None,
        "NpcFile": None,
        "Paper": stationery[k],
        "Letters": {},
    }
    dic["Letters"]["UsEnglish"] = {
        "Header": "",
        "Body": "",
        "Footer": "",
        "Sender": "",
    }
    with open(f"{k}.txt", "r") as f:
        readlines = f.readlines()

        i = sum(1 for _ in readlines)
        for j, line in enumerate(readlines):
            if j == 0:
                dic["Letters"]["UsEnglish"]["Header"] = line.replace("\n", "").replace("\\n", "\n")

            if j >= 2 and j < i - 1:
                dic["Letters"]["UsEnglish"]["Body"] += line.replace("\n", "") + "\n"

            if j == i - 1 and "Nintendo" not in line:
                dic["Letters"]["UsEnglish"]["Footer"] = line.replace("\n", "")
            else:
                dic["Letters"]["UsEnglish"]["Footer"] = "RiiConnect24"

        dic["Letters"]["UsEnglish"]["Body"] = dic["Letters"]["UsEnglish"]["Body"].replace("\n\n", "")
        dic["Letters"]["UsEnglish"]["Sender"] = "RiiConnect24"

        dic["Letters"]["EuEnglish"] = {}
        dic["Letters"]["EuEnglish"]["Header"] = dic["Letters"]["UsEnglish"]["Header"]
        dic["Letters"]["EuEnglish"]["Body"] = dic["Letters"]["UsEnglish"]["Body"]
        dic["Letters"]["EuEnglish"]["Footer"] = dic["Letters"]["UsEnglish"]["Footer"]
        dic["Letters"]["EuEnglish"]["Sender"] = dic["Letters"]["UsEnglish"]["Sender"]

    with open(f"{k}.json", "w") as f:
        json.dump(dic, f, indent=1)
