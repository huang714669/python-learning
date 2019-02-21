# -*- coding:utf-8 -*- 

import sys, getopt
import os

def usage():
	"""
The output  configuration file contents.

Usage: geely_logon.py -u <username> -p <password>
or:  geely_logon.py --username=<username> --password=<username>

Description
	        -u,--username your domain username.
	        -p,--password	your computer password.
	        -h,--help    Display help information.
for exampel
            python geely_logon.py -u huangzihao -p pwd
            python -h
"""

def logon(argv):
    username = ""
    password = ""
    if not argv:
        print("the parameters should be  provided")
        print(usage.__doc__)
        sys.exit(-2)
    try:
        opts, args = getopt.getopt(argv, "hu:p:",["help", "username=", "password="])

    except getopt.GetoptError  as err:
        print(err)
        print(usage.__doc__)
        sys.exit(-2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print(usage.__doc__)
            sys.exit()
        elif opt in ("-u", "--username") and arg:
            username = arg 
        elif opt in ("-p", "--password") and arg:
            password = arg
        else:
            print("Using the wrong way,please view the help information")
    if username and  password:
        logon = os.system("curl  -d 'opr=pwdLogin&userName=%s&pwd=%s&rememberPwd=0'  http://1.1.1.3/ac_portal/login.php" %(username, password))    
        print(logon)
    else:
        print(usage.__doc__)
        sys.exit(-2)

if __name__ == "__main__":
    logon(sys.argv[1:])
