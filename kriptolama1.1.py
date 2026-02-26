import pyAesCrypt
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox


# ŞİFRELEME FONKSİYONLARI

def sifrele(dosya, sifre):
    bufferSize = 512 * 1024
    sifreli_dosya = str(dosya) + ".aes"

    try:
        pyAesCrypt.encryptFile(str(dosya), sifreli_dosya, sifre, bufferSize)
        os.remove(dosya)
    except FileNotFoundError:
        messagebox.showerror("Hata", f"'{dosya}' adında bir dosya bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Şifreleme sırasında bir hata oluştu: {e}")

def sifrecoz(dosya, sifre):
    bufferSize = 512 * 1024
    if str(dosya).endswith(".aes"):
        cozulmus_dosya = str(dosya)[:-4]
    else:
        cozulmus_dosya = "cozulmus_" + str(dosya)

    try:
        pyAesCrypt.decryptFile(str(dosya), cozulmus_dosya, sifre, bufferSize)
        os.remove(dosya)
    except FileNotFoundError:
        messagebox.showerror("Hata", f"'{dosya}' adında bir dosya bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Şifre çözme sırasında bir hata oluştu: {e}")


# GUI ARA FONKSİYONLARI

def encrypt_ui():
    dosya = selected_file.get()
    sifre = password_entry.get()
    if dosya == "" or sifre == "":
        messagebox.showerror("Hata", "Dosya veya şifre boş olamaz.")
        return
    sifrele(dosya, sifre)
    messagebox.showinfo("Başarılı", f"Dosya şifrelendi: {dosya}.aes")

def decrypt_ui():
    dosya = selected_file.get()
    sifre = password_entry.get()
    if dosya == "" or sifre == "":
        messagebox.showerror("Hata", "Dosya veya şifre boş olamaz.")
        return
    sifrecoz(dosya, sifre)
    messagebox.showinfo("Başarılı", f"Dosya çözüldü: {dosya}")


# GUI PENCERE OLUŞTURMA

ctk.set_appearance_mode("Dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Tema rengi

app = ctk.CTk()
app.geometry("500x400")
app.title("AES Dosya Şifreleme")

selected_file = ctk.StringVar()

# Dosya seçme alanı
file_entry = ctk.CTkEntry(app, textvariable=selected_file, width=300)
file_entry.pack(pady=20)

file_button = ctk.CTkButton(app, text="Dosya Seç", command=lambda: selected_file.set(filedialog.askopenfilename()))
file_button.pack(pady=5)

# Şifre girişi
password_entry = ctk.CTkEntry(app, placeholder_text="Şifre girin", show="*")
password_entry.pack(pady=10)

# Şifrele / Çöz butonları
encrypt_button = ctk.CTkButton(app, text="Şifrele", command=encrypt_ui)
encrypt_button.pack(pady=5)

decrypt_button = ctk.CTkButton(app, text="Şifre Çöz", command=decrypt_ui)
decrypt_button.pack(pady=5)

app.mainloop()