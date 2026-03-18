index_data = {
    "A":1,
    "B":2,
    "C":3,
    "Ç":4,
    "D":5,
    "E":6,
    "F":7,
    "G":8,
    "Ğ":9,
    "H":10,
    "I":11,
    "İ":12,
    "J":13,
    "K":14,
    "L":15,
    "M":16,
    "N":17,
    "O":18,
    "Ö":19,
    "P":20,
    "R":21,
    "S":22,
    "Ş":23,
    "T":24,
    "U":25,
    "Ü":26,
    "V":27,
    "Y":28,
    "Z":29
}

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
                break
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

