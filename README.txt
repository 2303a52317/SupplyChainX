SUPPLYCHAINX - QUICK DEMO START (Windows PowerShell)

FASTEST WAY TO RUN:
1. Open PowerShell in this folder.
2. Activate your venv: .\venv\Scripts\Activate.ps1
   If you do not have one: py -3.12 -m venv venv
   then: .\venv\Scripts\Activate.ps1
3. Install demo dependencies:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
4. Run: python app.py
5. Open http://127.0.0.1:5000

This mode supports product registration, SQLite history, stage updates and QR codes.
Blockchain calls are optional and disabled until Web3.py, Ganache and a deployed contract
are configured. This lets you demonstrate the application without the lru-dict build issue.

OPTIONAL BLOCKCHAIN DEPENDENCY:
   python -m pip install -r requirements-blockchain.txt

If lru-dict fails, install Visual Studio Build Tools with Desktop development with C++,
MSVC C++ build tools and a Windows 10/11 SDK, or use a Python version with a compatible
prebuilt wheel. This is a classroom demo, not production software.
