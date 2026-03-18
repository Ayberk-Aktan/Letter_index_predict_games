import numpy as np 
from indexes import index_data

def first_game_choose():
    while True:
        print("/-----1.Oyun Modu------/") 

        try:
            game_right = int(input("Kaç Defa Oynamak İstiyorsunuz: ")) 
         
            computer_score = player_score = 0
            i = 1 

        except ValueError:
            print("Lütfen Alanları Boş Bırakmayınız ve Girdileri Doğru Giriniz.")
            continue 
        except KeyboardInterrupt:
            print("Menüye Yönlendiriliyorsunuz...")
            return 
        else:
            while i <= game_right:
                computer_random_index = np.random.randint(1,29)

                computer_choose_letter = index_data[computer_random_index] 
                
                try:
                    player_index_predict = int(input(f"{computer_choose_letter} Sence Kaçıncı İndextedir ? : ")) 
                    
                    if player_index_predict < 1 or player_index_predict > 29:
                        print("Üzgünüm Tekrar Deneyiniz [1,29] arasında sayı seçiniz") 
                        continue 
                except ValueError:
                    print("Lütfen Alanları Boş Bırakmayınız ve Girdileri Doğru Giriniz!") 
                    continue 
                except KeyboardInterrupt:
                    print("Menüye Yönlendiriliyorsunuz...")
                    return 
                else:
                    if computer_random_index == player_index_predict:
                        print("Oyuncu Kazandı ve Oyuncuya 5 puan verildi!")
                        player_score += 5 
                    else:
                        print("Bilgisayar Kazandı ve Bilgisayara 5 puan verildi!")
                        computer_score += 5 
                    

                    i += 1
            
            if computer_score > player_score:
                print(f"Skor Bilgisayar : {computer_score} - Oyuncu : {player_score}\n Oyunu Bilgisayar Kazandı") 
                print("Yeniden Oynamak İster misiniz ? ") 
            elif computer_score == player_score:
                print(f"Skor Bilgisayar : {computer_score} - Oyuncu : {player_score}\n Oyun Berabere!")
                print("Yeniden Oynamak İster misiniz ? ") 
            elif player_score > computer_score:
                print(f"Skor Bilgisayar : {computer_score} - Oyuncu : {player_score}\n Oyunu Oyuncu Kazandı")
                print("Yeniden Oynamak İster misiniz ?") 
            
            return

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
                first_game_choose()
            elif game_mode == 2:
                print("2.Mod Oyun Tercihi Yaptınız!") 
                break 

