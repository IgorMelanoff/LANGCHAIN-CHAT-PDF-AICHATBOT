Example of Question ot RAG:
Does Igor  in follow PDF resume has any AI experience?
Can you eright the cover letter for Automation Developer in Testing for Igor Emelyanov using the following PDF resume?


///////////Insatllation PYTHON evironment//////////
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
pip install faiss-cpu
pip install openai
pip install -U langchain-community
pip install tiktoken

6. create hidden file for API keys
touch .env

7. Git ignore file create -> got folder

touch .gitignore

8. Just copy to gitignore 
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

9. https://platform.openai.com/account/api-keys


10.streamlit run app.py
