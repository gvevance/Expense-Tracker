# https://coderslegacy.com/python/imap-read-emails-with-imaplib/
# todo deadline - skeleton of the project by 25th Dec

from setup import connect_to_server
from emails import parse_emails
from setup import return_message_id_dict

# return an imap connection object
connection = connect_to_server()
seen_messages_dict = return_message_id_dict()

#select INBOX
status,messages = connection.select("\"PhonePe sent or paid\"")
num_of_messages = int(messages[0])
parse_emails(connection,"\"PhonePe sent or paid\"",num_of_messages)

#select INBOX
status,messages = connection.select("\"Sodexo payments\"")
num_of_messages = int(messages[0])
parse_emails(connection,"\"Sodexo payments\"",num_of_messages)
            
''' read the latest k emails until you reach an email we've looked at before.
    store message-id or some value unique to an email in a dictionary.
    store this dictionary in a pickle object '''
