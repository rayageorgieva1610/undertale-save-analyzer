from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
save_path = base_dir / "data" / "file0"

with open(save_path, "r") as save_file:
    save_data = save_file.readlines()

name = save_data[0].strip()
lv = int(save_data[1].strip())
current_hp = int(save_data[2].strip())
max_hp = int(save_data[3].strip())
exp = int(save_data[9].strip())
gold = int(save_data[10].strip())
kills = int(save_data[11].strip())

print("\nUNDERTALE PLAYER STATS")
print("----------------------")
print(f"Name: {name}")
print(f"LV: {lv}")
print(f"HP: {current_hp}/{max_hp}")
print(f"EXP: {exp}")
print(f"Gold: {gold}")
print(f"Kills: {kills}")