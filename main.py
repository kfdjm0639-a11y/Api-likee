# main.py
import os
import sys
import importlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# إضافة مجلد المشروع إلى مسار Python
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# تحميل كل ملفات Python ما عدا main.py
for filename in os.listdir(BASE_DIR):
    if filename.endswith(".py") and filename != "main.py":
        module_name = filename[:-3]

        try:
            importlib.import_module(module_name)
            print(f"[OK] Loaded: {filename}")
        except Exception as e:
            print(f"[ERROR] {filename}: {e}")

# إذا كان app.py يحتوي على Flask app
try:
    from app import app
except ImportError:
    app = None


if __name__ == "__main__":
    if app is not None:
        port = int(os.environ.get("PORT", 8080))
        app.run(host="0.0.0.0", port=port)
    else:
        print("No Flask app found.")
