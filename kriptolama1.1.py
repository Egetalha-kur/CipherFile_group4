import pyAesCrypt
import os


def sifrele(dosya):
    bufferSize = 512 * 1024
    sifreli_dosya = str(dosya) + ".aes"

    # Şifre belirlerken boş geçilmesini engellemek için döngü
    while True:
        password = input("Sifre belirleyin: ")
        if password == "":
            print("[!] HATA: Sifre bos birakilamaz. Lutfen tekrar deneyin.\n")
        else:
            break

    try:
        # Şifreleme işlemini dene
        pyAesCrypt.encryptFile(str(dosya), sifreli_dosya, password, bufferSize)
        print(f"\n[+] BASARILI: Dosyaniz kriptolandi -> {sifreli_dosya}")

        # İşlem bitince orijinal dosyayı sil
        os.remove(dosya)
        print(f"[-] BILGI: Guvenlik amaciyla orijinal dosya ({dosya}) silindi.")

    except FileNotFoundError:
        print(f"\n[!] HATA: '{dosya}' adinda bir dosya bulunamadi.")
    except Exception as e:
        print(f"\n[!] BEKLENMEYEN HATA: Sifreleme sirasinda bir sorun olustu: {e}")


def sifrecoz(dosya):
    bufferSize = 512 * 1024

    if str(dosya).endswith(".aes"):
        cozulmus_dosya = str(dosya)[:-4]
    else:
        cozulmus_dosya = "cozulmus_" + str(dosya)

    # Şifreyi doğru girene kadar tekrar soracak döngü
    while True:
        password = input("Cozmek icin sifre girin (Iptal icin 'q' basabilirsiniz): ")

        if password.lower() == 'q':
            print("Islem iptal edildi.")
            break

        try:
            # Şifre çözme işlemini dene
            pyAesCrypt.decryptFile(str(dosya), cozulmus_dosya, password, bufferSize)
            print(f"\n[+] BASARILI: Kilit acildi -> {cozulmus_dosya}")

            # İşlem bitince kilitli (.aes) dosyayı sil
            os.remove(dosya)
            print(f"[-] BILGI: Temizlik amaciyla kilitli dosya ({dosya}) silindi.")
            break  # Şifre doğruysa ve işlem bittiyse döngüyü kır

        except ValueError:
            # Şifre yanlışsa veya dosya bozuksa burası çalışır
            print("\n[!] HATA: Yanlis sifre girdiniz veya dosya bozuk! Lutfen tekrar deneyin.\n")
        except FileNotFoundError:
            print(f"\n[!] HATA: '{dosya}' adinda bir dosya bulunamadi.")
            break  # Dosya yoksa döngüyü kır
        except Exception as e:
            print(f"\n[!] BEKLENMEYEN HATA: {e}")
            break


# --- ANA PROGRAM ---
print("\n-- KRIPTO PROGRAMINA HOS GELDIN --")

# Programın sürekli açık kalmasını sağlayan ana döngü
while True:
    print("\n" + "=" * 45)
    hedef_dir = input("Islem yapmak istediginiz dosyanin adini girin (Cikis icin 'q'): ")

    if hedef_dir.lower() == 'q':
        print("\nProgramdan cikiliyor. Gorusmek uzere!")
        break

    print("\nHangi islemi yapmak istiyorsun?")
    print("1 - Sifrele")
    print("2 - Sifre Coz")

    # Kullanıcı doğru işlem seçeneğini girene kadar dönecek döngü
    while True:
        secim = input("Secim yapiniz (1 veya 2): ")

        if secim == "1":
            sifrele(hedef_dir)
            break
        elif secim == "2":
            sifrecoz(hedef_dir)
            break
        else:
            print("[!] HATA: Hatali secim yaptiniz. Lutfen sadece 1 veya 2 girin.\n")