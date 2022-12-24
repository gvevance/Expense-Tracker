# methods to parse and read the relevant emails
import email

def parse_emails(connection,inboxname,num_of_messages) :
    
    if inboxname == "\"PhonePe sent or paid\"" :
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

    if inboxname == "\"Sodexo payments\"" :
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