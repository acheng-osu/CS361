import time
from pathlib import Path
import os


while True:
    time.sleep(1)

    img_service_file = open('image-service.txt', 'r+', encoding="utf-8")
    data = img_service_file.read()

    if data.isnumeric():
        time.sleep(3)
        img_service_file.close()
        img_service_file = open('image-service.txt', 'w', encoding="utf-8")

        list_imgs = os.listdir(path="imgs")
        img_index = int(data) % len(list_imgs)

        str_path = str(Path.cwd()) + "/imgs/" + list_imgs[img_index]

        time.sleep(3)
        img_service_file.write(str_path)

        img_service_file.close()


