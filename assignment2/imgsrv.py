import time
from pathlib import Path
import os


while True:
    time.sleep(1)

    with open('image-service.txt', 'r+', encoding="utf-8") as img_service_file:
        data = img_service_file.read()

        if data.isnumeric():
            list_imgs = os.listdir(path="imgs")
            img_index = int(data) % len(list_imgs)

            str_path = str(Path.cwd()) + "/imgs/" + list_imgs[img_index]
            
            img_service_file.seek(0)
            img_service_file.truncate()
            img_service_file.write(str_path)

