 # -*- coding: utf-8
 # open source don't forget to give a star
 # angga Kurniawan (fb.me/onyedikachi.okoro.3760)
 import os,sys,time
 from platform import system

 logo = """     \033[0;91m██████  ██    ██ ███████ ███    ██  ██████ 
     \033[0;91m██   ██  ██  ██  ██      ████   ██ ██      
     \033[0;91m██████    ████   █████   ██ ██  ██ ██      
     \033[0;97m██         ██    ██      ██  ██ ██ ██      
     \033[0;97m██         ██    ███████ ██   ████  ██████ 
 ---------------------------------------------------
 ➣ Author    : KACHI
 ➣ GitHub    : https://github.com/Kachilee1
 ---------------------------------------------------
 ➣ Instagram : @kachilee1
 ➣ Facebook  : https://fb.me/onyedikachi.okoro.3760\n"""

 defmenu():
 os.system("clear")
 print logo
 print "[!] Enter the file name without .py"
 print "[*] Example: pyenc.py (insert file: pyenc)"
 name_files = raw_input(" [+] Input File : ")
 sv_file = raw_input(" [+] Save File : ")
 py_datt = (str(name_files)+".pyo")
 print " [#] Encrypt the SC soon..."
 time.sleep(1)
 os.system('python2 -OO -m py_compile ' + name_files+'.py')
 os.system("mv "+str(py_datt)+" "+str(sv_file)+".py")
 print "[*] Ok Encrypted"
 print " [+] Filename : "+str(sv_file)+".py"

 if __name__ == '__main__':
 menu()
