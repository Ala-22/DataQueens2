
import webbrowser
import os
import time

# 1. طباعة شيء وهمي للضحية
print("Loading Movie Player...")
time.sleep(2) 
print("Connecting to server...")
time.sleep(1)

# 2. الخدعة: فتح صفحة الرعب فجأة في المتصفح
# نحصل على مسار الصفحة الحالي
current_dir = os.getcwd()
html_file = os.path.join(current_dir, "index.html")

# فتح الصفحة في المتصفح الافتراضي
print("⚠️ ERROR: Connection Interrupt!")
webbrowser.open(f"file://{html_file}")
