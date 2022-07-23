import requests
import os
import os.path
import re
import shutil


url = "https://tabletopaudio.com"
html_path = "tabletopaudio.com.html"
download_dest = "./out"


# -- Getting html of page with all tracks
if not os.path.exists(html_path):
    html = requests.get(url).text
    with open("tabletopaudio.com.html", mode="w") as f:
        f.write(html)
else:
    with open("tabletopaudio.com.html", mode="r") as f:
        html = f.read()

# -- Find all tracks
exp = re.compile("saveAs\('\d\d\d_\w*'\)")
track_names = [m.removeprefix("saveAs('")[:-2] for m in exp.findall(html)]


# -- Start to download all tracks

if not os.path.exists(download_dest):
    os.mkdir(download_dest)

downloaded_tracks = re.compile("\w*.mp3").findall(" ".join(os.listdir(download_dest)))
downloaded_count = len(track_names)


for index, track_name in enumerate(track_names):
    if track_name in downloaded_tracks:
        downloaded_count -= 1
        continue

    print(f"Downloading track '{track_name}' [{index + 1}/{downloaded_count}]")
    track_dest = os.path.join(download_dest, track_name + ".mp3")
    print(f"curl https://sounds.tabletopaudio.com/{track_name} --output {track_dest}")
    break
