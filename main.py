import random
import os
from time import sleep

os.system("cls")

def yazi_or_tura():
    yazi_tura = ['Yazı', 'Tura']
    return random.choices(yazi_tura, [1, 1])[0]

print("Oynamak için 1 rakamını yazın.")
print("")
choice = int(input("> "))
os.system("cls")

while True:
    if choice == 1:
        print("Sonuç:", yazi_or_tura())
        print("")
        print("Tekrar oynamak için 1 rakamını yazın.")
        print("Çıkmak için 2 rakamını yazın")
        print("")
        end_game_choice = int(input(("> ")))

        if end_game_choice == 1:
            os.system("cls")
            continue
        
        elif end_game_choice == 2:
            os.system("cls")
            break
        
        else:
            os.system("cls")
            print("(!) Hata")
            sleep(2)
            os.system("cls")
            break

    else:
        os.system("cls")
        print("(!) Hata")
        sleep(2)
        os.system("cls")
        break