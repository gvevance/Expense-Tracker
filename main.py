# https://github.com/gvevance/Expense-Tracker
# https://coderslegacy.com/python/imap-read-emails-with-imaplib/ => old python version
#! deadline - skeleton of the project by 29th Dec
#! Learn and set up logger for commandline logging

from setup import connect_to_server
from setup import get_seen_message_ids
from email_parse import get_message_ID
from email_parse import parse_PhonePe_email
from email_parse import parse_Sodexo_email
from setup import update_seen_message_ids

TESTING = False

# return an imap connection object
connection = connect_to_server()
seen_messages_dict = get_seen_message_ids()

if TESTING :
    seen_messages_dict = {}

if TESTING :
    print("\nDisplay dict before main logic run\n")
    for x in seen_messages_dict :
        print(x)
    print("\n")

#select INBOX for PhonePe
status,messages = connection.select("\"PhonePe sent or paid\"")
num_of_messages = int(messages[0])

if TESTING :
    num_of_messages = 1

for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        parse_PhonePe_email(msg)
    else :
        print("PhonePe payments processed.")
        break

#select INBOX for Sodexo
status,messages = connection.select("\"Sodexo payments\"")
num_of_messages = int(messages[0])

if TESTING :
    num_of_messages = 1

for i in range(num_of_messages,0,-1):
    res, msg, msg_ID = get_message_ID(connection,i)
    if msg_ID not in seen_messages_dict :
        seen_messages_dict[msg_ID] = True
        parse_Sodexo_email(msg)
    else :
        print("Sodexo payments processed.")
        break

if TESTING :
    print("\nDisplay dict after logic run\n")
    for x in seen_messages_dict :
         print(x)

update_seen_message_ids(seen_messages_dict )