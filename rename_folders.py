import os, shutil

base = "LandingDataset"

folder_map = {
    "aerial view road drone":        "road",
    "aerial view forest drone":      "forest",
    "aerial view grass field drone": "grass",
    "aerial view building rooftop":  "building",
    "aerial view water lake drone":  "water",
    "aerial view rocky terrain":     "rocky",
}

for old_name, new_name in folder_map.items():
    old_path = os.path.join(base, old_name)
    new_path = os.path.join(base, new_name)
    if os.path.exists(old_path):
        files = os.listdir(old_path)
        for f in files:
            src = os.path.join(old_path, f)
            dst = os.path.join(new_path, f)
            shutil.move(src, dst)
        os.rmdir(old_path)
        print(f"✓ Moved {len(files)} images: {old_name} → {new_name}")
    else:
        print(f"✗ Not found: {old_name}")

print("\nDone! Checking counts:")
for folder in ["road","forest","grass","building","water","rocky"]:
    path = os.path.join(base, folder)
    count = len(os.listdir(path)) if os.path.exists(path) else 0
    print(f"  {folder}: {count} images")