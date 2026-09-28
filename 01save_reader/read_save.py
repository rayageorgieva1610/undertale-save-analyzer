from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
save_path = base_dir / "data" / "file0"

with open(save_path, "r") as save_file:
    save_data = save_file.readlines()

print(f"Save file contains {len(save_data)} lines.\n")

for line_number, value in enumerate(save_data, start=1):
    print(f"Line {line_number}: {value.strip()}")