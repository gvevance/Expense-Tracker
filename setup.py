import imaplib, pickle
from os.path import exists

LOGIN_FILE = "login.txt"
PICKLE_OBJ_FILE = "seen_message_IDs.pkl"
CSV_FILE = "transactions.csv"

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
    
    print("Connection established.")
    return connection


def get_seen_message_ids ():
    
    if not exists(PICKLE_OBJ_FILE) :
        empty_dic ={}
        with open(PICKLE_OBJ_FILE,'wb') as file :
            pickle.dump(empty_dic,file)
                        
    with open(PICKLE_OBJ_FILE,'rb') as file :
        data = pickle.load(file)
    
    return data


def update_seen_message_ids (updated_dict):
    with open(PICKLE_OBJ_FILE,'wb') as file :
        pickle.dump(updated_dict,file)


def setup_csv() :
    if not exists(CSV_FILE) :
        with open(CSV_FILE,'wb+') as file :
            pass
    return CSV_FILE
    
