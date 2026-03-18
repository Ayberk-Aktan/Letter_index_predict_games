from games import game_choose

def menu():
    while True:
        print("/-----HARF İNDEX TAHMİN OYUNU-----/") 
        print("""
        1-) Oyuna Başlayın \n
        2-) Nasıl Oynanır ? \n
        3-) Çıkış Yap \n
        """)

        try:
            menu_options = int(input("Lütfen Seçim Yapınız: "))
        except ValueError:
            print("Lütfen Alanı Boş Bırakmayınız ve Girdileri Doğru Giriniz.")
            continue 
        except KeyboardInterrupt:
            print("\nOyundan Çıkış Yaptınız!")
            break 
        else:
            if menu_options not in [1,2,3]:
                print("HATALI KOMUT!!")
                continue 
            elif menu_options == 1:
                print("Oyuna Başlıyorsunuz")
                game_choose()
            elif menu_options == 2:
                print("Nasıl Oynanır ?") 
                print("""
                1.Modda bilgisayar kullanıcı için rastgele bir harf seçecek ve kullanıcı ise o harfin kaçıncı indexte olduğunu bulmaya çalışacak.
                Eğer ki kullanıcı doğru tahmin yaparsa 5 puan yapamazsa bilgisayar 5 puan kazanacaktır. Kazanan durumu ise belirlenen tur sonunda belli olacaktır.
                """)
                print("""
                2.Modda bilgisayar kullanıcı için rastgele bir harf sayı seçecek (1-29 arasında) ve kullanıcı ise o indexte hangi harfe karşılık geldiğini tahmin etmeye çalışacak.
                Eğer ki kullanıcı doğru tahmin yaparsa 5 puan yapamazsa bilgisayar 5 puan kazanacaktır. Kazanan durumu ise belirlenen tur sonunda belli olacaktır.
                """)
                continue
            elif menu_options == 3:
                print("Oyundan Çıkış Yapıyorsunuz...")
                return exit() 
    
menu()

