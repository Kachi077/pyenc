import compileall
import os,sys,time
from datetime import datetime
os.system('pip install uncompyle6')
a = datetime.now().strftime('%Y-%m-%d %H:%M')
os.system('git pull')
logo = """
 \033[1;31;40m/$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$
\033[1;32;40m| $$  /$$/ /$$__  $$ /$$__  $$| $$  | $$|_  $$_/
\033[1;33;40m| $$ /$$/ | $$  \ $$| $$  \__/| $$  | $$  | $$  
\033[1;34;40m| $$$$$/  | $$$$$$$$| $$      | $$$$$$$$  | $$  
\033[1;35;40m| $$  $$  | $$__  $$| $$      | $$__  $$  | $$ \033[1;31m    Created by Kachi\t\033[1;36m 
\033[1;36;40m| $$\  $$ | $$  | $$| $$    $$| $$  | $$  | $$  
\033[1;31;40m| $$ \  $$| $$  | $$|  $$$$$$/| $$  | $$ /$$$$$$
\033[1;35;40m|__/  \__/|__/  |__/ \______/ |__/  |__/|______/
"""
os.system('clear')
print(logo)
print('\033[1;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++'),time.sleep(0.3)
print('\033[1;31m[1] \033[1;36mEncrypt | py to pyc'),time.sleep(0.3)
print('\033[1;31m[2] \033[1;35mDecode  | pyc to py'),time.sleep(0.3)
print('\033[1;36m+++++++++++++++++++++++++++++++++++++++'+a),time.sleep(0.3)
choose =input('\n\033[1;31m[?]Choose : \033[1;37m')
if choose =='1':
    file_py = input("\n\033[1;32mFile >\033[1;37m")
    compileall.compile_file(file_py)
    print('\033[1;31msuccess encrypt')
    print("\033[1;36mSave to __pycache__")
elif choose =='2':
    file_pyc = input('\n\033[1;32mFile >\033[1;37m')
    com = f'uncompyle6 {file_pyc} > dec.py'
    os.system(com)
    print('\033[1;31mdecoding success')
else:
    print('\033[1;31mplease choose 1 or 2 !')


