# bentar gw lupa 😂🤣
# okay gw inget sekarang hahahaha.

import subprocess
import time
import os

if not os.path.exists("hasilDownload"):
  os.makedirs("hasilDownload")

subprocess.run(["clear"])
time.sleep(1)
print("tunggu bos")
print("")
time.sleep(2)
data = input("masukan link yt: ")
print("")
if not data:
  print("tolong masukan link/urlnya!")
else:
  print("")
  subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", "hasilDownload/%(title)s.%(ext)s", data])
  print("")
  print("PERINTAH SELESAI")

# 😂🤣😭
