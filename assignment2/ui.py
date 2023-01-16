import time

while True:
    user_choice = input("Please enter 1 to generate a new image or 2 to exit the program: ")

    if user_choice == "1":
        prng_service_file = open('prng-service.txt', 'w', encoding="utf-8")
        prng_service_file.write("run")
        prng_service_file.close()

        time.sleep(10)

        prng_service_file = open('prng-service.txt', 'r', encoding="utf-8")
        str_rand = prng_service_file.read()
        prng_service_file.close()

        img_service_file = open('image-service.txt', 'w', encoding="utf-8")
        img_service_file.write(str_rand)
        img_service_file.close()

        time.sleep(10)

        img_service_file = open('image-service.txt', 'r', encoding="utf-8")
        img_path = img_service_file.read()
        img_service_file.close()
        print("\n" + img_path + "\n")
    elif user_choice == "2":
        print("Thank you. Goodbye.")
        break
    else:
        print("I do not recognize that input. Please input either \"1\" or \"2\"")