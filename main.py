# https://coderslegacy.com/python/imap-read-emails-with-imaplib/
# todo deadline - skeleton of the project by 25th Dec

from setup import connect_to_server
import email

# return an imap connection object
connection = connect_to_server()

#select INBOX
status,messages = connection.select("\"PhonePe sent or paid\"")
num_of_messages = int(messages[0])

for i in range(num_of_messages,0,-1):
    res, msg = connection.fetch(str(i), '(RFC822)')
    for response in msg :
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject, encoding = email.header.decode_header(msg["Subject"])[0]
            if isinstance(subject,bytes):
                subject = subject.decode(encoding)
                
            From, encoding = email.header.decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            
            print("ID:",str(i))
            print("Subject:", subject)
            print("From:", From)
            print()

status,messages = connection.select("\"Sodexo payments\"")
num_of_messages = int(messages[0])

for i in range(num_of_messages,0,-1):
    res, msg = connection.fetch(str(i), '(RFC822)')
    for response in msg :
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject, encoding = email.header.decode_header(msg["Subject"])[0]
            if isinstance(subject,bytes):
                subject = subject.decode(encoding)
                
            From, encoding = email.header.decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
             
            print("ID:",str(i))
            print("Subject:", subject)
            print("From:", From)
            print()

            
# todo figure out preventing duplicate entries
# todo Idea 1 : each email has an ID - store it locally in a pickle format
# 