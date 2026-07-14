from bing_image_downloader import downloader
import os, shutil

os.makedirs("testImages", exist_ok=True)

queries = [
    ("aerial drone road view test",     "test_road"),
    ("aerial drone forest view test",   "test_forest"),
    ("aerial drone water lake test",    "test_water"),
    ("aerial drone grass field test",   "test_grass"),
    ("aerial drone rocky terrain test", "test_rocky"),
    ("aerial drone building roof test", "test_building"),
]

for query, save_name in queries:
    downloader.download(query, limit=3, output_dir='temp_test',
                       adult_filter_off=True, force_replace=False,
                       timeout=60, verbose=False)
    folder = os.path.join('temp_test', query)
    if os.path.exists(folder):
        files = os.listdir(folder)
        if files:
            src = os.path.join(folder, files[0])
            dst = os.path.join('testImages', save_name + os.path.splitext(files[0])[1])
            shutil.copy(src, dst)
            print(f"✓ Saved: {save_name}")

shutil.rmtree('temp_test', ignore_errors=True)
print("\nTest images ready in testImages folder!")