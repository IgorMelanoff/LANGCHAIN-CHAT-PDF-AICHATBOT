1. Install VS
2. Install Python Ms Extention
3. Check in VS Terminal:
python3 --version
4. Create the environment
python3 -m venv .venv
4.1. Activate the .vent   
source .venv/bin/activate 
5. pip3 --version 
4. Update pip to the newest version: 
python3 -m pip install --upgrade pip

5.Install packages for Langchain and streamLit
pip3 install langchain pypdf2 python-dotenv streamlit


6. Git ignore file create -> got folder

touch .gitignore

7. Just copy to gitignore 
////////////

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
.venv/
.env/
venv/
ENV/

# VS Code settings
.vscode/

# PyCharm settings
.idea/

# Mac specific files
.DS_Store

/////////////////