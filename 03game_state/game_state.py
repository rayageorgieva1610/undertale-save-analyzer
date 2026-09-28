from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
save_path = base_dir / "data" / "file0"

with open(save_path, "r") as save_file:
    save_data = save_file.readlines()

lv = int(save_data[1].strip())
exp = int(save_data[9].strip())
kills = int(save_data[11].strip())

# Area kill counters
ruins_kills = int(save_data[232].strip())
snowdin_kills = int(save_data[233].strip())
waterfall_kills = int(save_data[234].strip())
hotland_kills = int(save_data[235].strip())

# Genocide route requirements
genocide_requirements = [
    (ruins_kills >= 20, "Ruins kill requirement"),
    (int(save_data[75].strip()) == 4, "Toriel"),
    (int(save_data[82].strip()) == 1, "Doggo"),
    (int(save_data[83].strip()) == 1, "Dogamy and Dogaressa"),
    (int(save_data[84].strip()) == 1, "Greater Dog"),
    (int(save_data[87].strip()) == 2, "Snowdrake"),
    (snowdin_kills >= 16, "Snowdin kill requirement"),
    (int(save_data[97].strip()) == 1, "Papyrus"),
    (int(save_data[111].strip()) == 1, "Shyren"),
    (int(save_data[282].strip()) == 1, "Glad Dummy"),
    (waterfall_kills >= 18, "Waterfall kill requirement"),
    (int(save_data[281].strip()) == 1, "Undyne the Undying"),
    (int(save_data[432].strip()) == 1, "Royal Guards"),
    (int(save_data[427].strip()) == 1, "Muffet"),
    (hotland_kills >= 40, "Hotland/CORE kill requirement"),
    (int(save_data[455].strip()) == 1, "Mettaton NEO")
]

# Calculate Murder Level
murder_level = 0

for requirement, description in genocide_requirements:
    if requirement:
        murder_level += 1
    else:
        break

# Determine current route status
if murder_level > 0:
    route = "Genocide"
    explanation = "Genocide requirements are currently being completed in order."

elif kills == 0 and exp == 0 and lv == 1:
    route = "Pacifist-compatible"
    explanation = "No EXP has been gained and no monsters have been killed."

else:
    route = "Neutral"
    explanation = "This save does not currently satisfy the Genocide or no-kill conditions."

print("\nUNDERTALE ROUTE ANALYSIS")
print("------------------------")

print(f"LV: {lv}")
print(f"EXP: {exp}")
print(f"Kills: {kills}")

print("\nGenocide Progress:")
print(f"Ruins:        {ruins_kills} / 20")
print(f"Snowdin:      {snowdin_kills} / 16")
print(f"Waterfall:    {waterfall_kills} / 18")
print(f"Hotland/CORE: {hotland_kills} / 40")

print(f"\nMurder Level: {murder_level}")

print(f"\nCurrent route status: {route}")
print(explanation)