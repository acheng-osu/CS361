import time
import random


while True:
    time.sleep(1)
    
    prng_service_file = open('prng-service.txt', 'r', encoding="utf-8")
    data = prng_service_file.read()

    if data == "run":
        time.sleep(3)
        prng_service_file.close()
        prng_service_file = open('prng-service.txt', 'w', encoding="utf-8")
        time.sleep(3)
        prng_service_file.write(str(random.randint(0, 10^6)))
        prng_service_file.close()
            






