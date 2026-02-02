import tkinter as tk
import datetime


# ==========================================
# Developer: Hadeel
# Module: Graphical User Interface (GUI)
# ==========================================

def create_ransom_window(decrypt_callback):
    """
    وظيفة هديل: بناء الواجهة الحمراء والعداد
    """
    root = tk.Tk()
    root.title("Ransomware Attack Simulation")
    root.geometry("600x450")
    root.configure(bg='#200000')  # خلفية حمراء داكنة

    # النصوص المرعبة
    tk.Label(root, text="☠️ YOUR FILES ARE HACKED ☠️", font=("Impact", 22), fg="red", bg='#200000').pack(pady=20)

    msg = """All your photos and documents are encrypted.
    You cannot access them anymore.

    To get the password, send $300 immediately."""
    tk.Label(root, text=msg, font=("Arial", 11), fg="white", bg='#200000', justify="center").pack()

    # العداد التنازلي
    time_label = tk.Label(root, text="24:00:00", font=("Consolas", 20, "bold"), fg="yellow", bg='#200000')
    time_label.pack(pady=15)

    def update_timer(seconds_left=86400):
        if seconds_left > 0:
            display = str(datetime.timedelta(seconds=seconds_left))
            time_label.config(text=f"Time Left: {display}")
            root.after(1000, update_timer, seconds_left - 1)
        else:
            time_label.config(text="TIME OVER! FILES LOST!", fg="red")

    update_timer()

    # زر فك التشفير (يربط مع وظيفة أسيل لاحقاً)
    tk.Button(root, text="🔓 UNLOCK FILES", command=decrypt_callback, bg="red", fg="white", font=("Arial", 12, "bold"),
              padx=20).pack(pady=30)

    return root
