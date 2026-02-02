from cryptography.fernet import Fernet
import os


# ==========================================
# Developer: Aseel
# Module: Decryption & Recovery
# ==========================================

def decrypt_files(files_list, key):
    """
    وظيفة أسيل: فك تشفير الملفات واستعادتها
    """
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

