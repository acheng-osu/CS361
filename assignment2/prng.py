import time
import random
import os


while True:
    time.sleep(1)
    
    with open('prng-service.txt', 'r+', encoding="utf-8") as prng_service_file:
        data = prng_service_file.read()
        
        if data == "run":
            list_imgs = os.listdir(path="imgs")
            num_rand = random.randint(0, len(list_imgs) - 1)
            prng_service_file.seek(0)
            prng_service_file.truncate()
            prng_service_file.write(str(num_rand))
            






