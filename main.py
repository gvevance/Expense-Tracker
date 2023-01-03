# https://github.com/gvevance/Expense-Tracker
# https://coderslegacy.com/python/imap-read-emails-with-imaplib/ => old python version
#! deadline - skeleton of the project by 29th Dec
#! Learn and set up logger for commandline logging

from setup import connect_to_server
from setup import get_seen_message_ids
from email_parse import get_message_ID
from email_parse import parse_PhonePe_email_1
from email_parse import parse_PhonePe_email_2
from email_parse import parse_Sodexo_email
from setup import update_seen_message_ids


# return an imap connection object
try :
    connection = connect_to_server()
# except socket.gaierror :
    # print("[Errno -3] Temporary failure in name resolution.")
except :    
    print("Some other error.")

seen_messages_dict = get_seen_message_ids()

#select INBOX for PhonePe sent or paid
status,messages = connection.select("\"PhonePe sent or paid\"")
num_of_messages = int(messages[0])

num_of_messages = 0     #todo comment
for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        # parse_PhonePe_email_1(msg)
    else :
        # print("PhonePe payments processed.")
        break

# #select INBOX for PhonePe Payment for
status,messages = connection.select("\"PhonePe Payment for\"")
num_of_messages = int(messages[0])

num_of_messages = 0     #todo comment
for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        parse_PhonePe_email_2(msg)
    else :
        print("PhonePe payments processed.")
        break


seen_messages_dict = {}     #todo comment
#select INBOX for Sodexo
status,messages = connection.select("\"Sodexo payments\"")
num_of_messages = int(messages[0])


# num_of_messages = 1     #todo comment
for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        parse_Sodexo_email(msg)
    else :
        print("Sodexo payments processed.")
        break

#todo uncomment
# update_seen_message_ids(seen_messages_dict)