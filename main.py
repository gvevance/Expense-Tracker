import subprocess
subprocess.call("pwd")

# email. detect subject.

import imaplib,email

'''comment out later'''
import sys
applic_spec_password = sys.argv[1]
'''comment out later'''

imap_url = "imap.gmail.com"
email = 'gvevance@gmail.com'

def connect_to_server(imap_url,user,password):
    ''' connecting to server '''
    connection = imaplib.IMAP4_SSL(imap_url)
    try :
        connection.login(user,password)

    except Exception as e:
        print(e)
        exit()
    
    return connection

a = connect_to_server(imap_url,email,applic_spec_password)
print(a)