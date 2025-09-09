# ⚙️ How to Create a Virtual Environment in VS Code

```bash
# 📂 1. Create project folder
mkdir my-project
cd my-project

# 🐍 2. Create virtual environment
python -m venv alliaz-day-1

# ▶️ 3. Activate virtual environment
# On Windows
.\alliaz-day-1\Scripts\Activate

# On macOS/Linux
source alliaz-day-1/bin/activate

# 📄 4. Create requirements.txt (inside project folder)


# ✏️ 5. Update requirements.txt with your needed packages

# 📦 6. Install all packages from requirements.txt
pip install -r requirements.txt

# 7. Type Ctrl+Shift+P ->  “Python: Select Interpreter” and select the one that points to your new virtual environment

# 8. •	If virtual environment not founded then find the path will include your folder and .<venv>\Scripts\python.exe
