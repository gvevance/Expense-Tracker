# https://github.com/gvevance/Expense-Tracker
# https://coderslegacy.com/python/imap-read-emails-with-imaplib/ => old python version
#todo define rules to categories transactions
#! Learn and set up logger for commandline logging

from setup import connect_to_server
from setup import get_seen_message_ids
from email_parse import get_message_ID
from email_parse import parse_PhonePe_email_1
from email_parse import parse_PhonePe_email_2
from email_parse import parse_Sodexo_email
from setup import update_seen_message_ids
from tabulate import process_transaction
from setup import setup_csv
from tabulate import dump_from_csv_file
from tabulate import dump_to_csv_file

verbose = False

# return an imap connection object
try :
    connection = connect_to_server()
# except socket.gaierror :
    # print("[Errno -3] Temporary failure in name resolution.")
except :    
    print("Some other error.")
    exit()

seen_messages_dict = get_seen_message_ids()
CSV_FILE = setup_csv()
BUFFER = []

seen_messages_dict = {}     # todo comment

#select INBOX for PhonePe sent or paid
status,messages = connection.select("\"PhonePe sent or paid\"")
num_of_messages = int(messages[0])
print("\n# of PhonePe type 1 emails :",num_of_messages)

# num_of_messages = 0     #todo comment
for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        details_dict = parse_PhonePe_email_1(msg,verbose)
        BUFFER = process_transaction(details_dict,BUFFER,verbose)
    else :
        # print("PhonePe payments processed.")
        break

# #select INBOX for PhonePe Payment for
status,messages = connection.select("\"PhonePe Payment for\"")
num_of_messages = int(messages[0])
print("\n# of PhonePe type 2 emails :",num_of_messages)

# num_of_messages = 0     #todo comment
for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        details_dict = parse_PhonePe_email_2(msg,verbose)
        BUFFER = process_transaction(details_dict,BUFFER,verbose)
    else :
        print("PhonePe payments processed.")
        break

#* bug fix - can be removed later when at least one message of this type has been received
if num_of_messages == 0 :
    print("PhonePe payments processed.")


seen_messages_dict = {}     #todo comment
#select INBOX for Sodexo
status,messages = connection.select("\"Sodexo payments\"")
num_of_messages = int(messages[0])
print("\n# of Sodexo emails :",num_of_messages)

num_of_messages = 0     #todo comment
for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        details_dict = parse_Sodexo_email(msg,verbose)
        BUFFER = process_transaction(details_dict,BUFFER,verbose)
    else :
        print("Sodexo payments processed.")
        break

#todo uncomment
update_seen_message_ids(seen_messages_dict)

if verbose :
    for item in BUFFER :
        print(item)

dump_to_csv_file(BUFFER,CSV_FILE)
dump_from_csv_file(CSV_FILE)