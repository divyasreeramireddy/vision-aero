import os, shutil, random

source = "C:\\safedrone_ai\\Aerial_Landscapes"
dest   = "C:\\safedrone_ai\\LandingDataset"

mapping = {
    "grass":    ["Grassland"],
    "forest":   ["Forest"],
    "building": ["City"],
    "water":    ["Lake"],
    "rocky":    ["Desert"],
    "road":     ["Highway"],
}

# Clean existing folders
for folder in mapping.keys():
    path = os.path.join(dest, folder)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    print(f"Cleaned: {folder}")

# Copy images
for class_name, source_folders in mapping.items():
    dest_path = os.path.join(dest, class_name)
    total = 0
    for src_folder in source_folders:
        src_path = os.path.join(source, src_folder)
        if not os.path.exists(src_path):
            print(f"Not found: {src_folder}")
            continue
        files = [f for f in os.listdir(src_path)
                 if f.endswith(('.jpg','.jpeg','.png','.webp'))]
        # Take max 200 images per class
        files = files[:150]
        for f in files:
            src  = os.path.join(src_path, f)
            dst  = os.path.join(dest_path, f"{src_folder}_{f}")
            shutil.copy(src, dst)
            total += 1
    print(f"✓ {class_name}: {total} images copied")

print("\nFinal counts:")
for folder in mapping.keys():
    path  = os.path.join(dest, folder)
    count = len(os.listdir(path))
    print(f"  {folder}: {count} images")

print("\nDataset ready!")