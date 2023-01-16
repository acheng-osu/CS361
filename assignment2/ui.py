import time

while True:
    user_choice = input("Welcome to Albert's Assignment 2.\nPlease enter 1 to generate a new image or 2 to exit the program: ")

    if user_choice == "1":
        with open('prng-service.txt', 'r+', encoding="utf-8") as prng_service_file:
            prng_service_file.seek(0)
            prng_service_file.truncate()

            prng_service_file.write("run")
            time.sleep(5)
            prng_service_file.seek(0)

            str_rand = int(prng_service_file.readline())
            with open('image-service.txt', 'r+', encoding="utf-8") as img_service_file:
                img_service_file.seek(0)
                img_service_file.truncate()

                img_service_file.write(str_rand)
                time.sleep(5)

                img_service_file.seek(0)
                print(img_service_file.read())
    elif user_choice == "2":
        print("Thank you. Goodbye.")
        break
    else:
        print("I do not recognize that input. Please input either \"1\" or \"2\"")