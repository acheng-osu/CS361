import time
import random
import os


while True:
    time.sleep(1)
    
    prng_service_file = open('prng-service.txt', 'r', encoding="utf-8")
    data = prng_service_file.read()

    if data == "run":
        prng_service_file.close()
        prng_service_file = open('prng-service.txt', 'w', encoding="utf-8")
        prng_service_file.write(random.randint(0, 10^6))
        prng_service_file.close()
            






