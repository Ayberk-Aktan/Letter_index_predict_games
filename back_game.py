def back_game():
    while True:
        try:
            choose_menu = input("Bir Daha Oyun Oynamak İster misiniz ? (e/h) : ").lower().strip() 
        except KeyboardInterrupt:
            print("Menüye Dönüyorsunuz...")
            return 
        else:
            if len(choose_menu) == 0:
                print("Lütfen Bu Alanı Doldurunuz!")
                continue 

            if choose_menu == "e":
                print("Oyuna Devam Ediyorsunuz...")
                return True 
            elif choose_menu == "h":
                print("Oyun Menüsüne Dönüyorsunuz...")
                return False
            else:
                print("HATA!! Lütfen Tekrar Deneyiniz!")
                continue 