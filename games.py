from indexes import index_data

def game_choose(): 
    while True:
        print("Oyuna Hoşgeldiniz! Oyun Modu Seçiniz") 

        try:
            game_mode = int(input("Oyun Modu Seçiniz: ")) 
        except ValueError:
            print("Lütfen Alanı Boş Bırakmayınız ve Girdileri Doğru Giriniz.") 
            continue
        except KeyboardInterrupt:
            print("\nMenüye Yönlendiriliyorsunuz...")
            break
        else:
            if game_mode not in [1,2]:
                print("HATA! Lütfen Doğru Seçim Yapınız!")
                continue 
            elif game_mode == 1:
                print("1.Mod Oyun Tercihi Yaptınız!") 
                break 
            elif game_mode == 2:
                print("2.Mod Oyun Tercihi Yaptınız!") 
                break 
    
