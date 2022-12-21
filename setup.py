import imaplib
LOGIN_FILE = "login.txt"

def connect_to_server():

    with open(LOGIN_FILE,"r") as loginfile :
        lines = loginfile.read().splitlines()
    
    imap_url = lines[0]
    email = lines[1]
    app_password = lines[2]
    
    connection = imaplib.IMAP4_SSL(imap_url)
    try :
        connection.login(email,app_password)

    except Exception as e:
        print(e)
        exit()
    
    return connection