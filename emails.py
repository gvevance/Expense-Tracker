# methods to parse and read the relevant emails
import email
from email.parser import BytesParser, Parser
from email.policy import default

parser = BytesParser()

def get_message_ID(connection,i) :
    res, msg = connection.fetch(str(i), '(RFC822)')
    msg_ID = '0'
    
    # for response in msg:
    #     if isinstance(response, tuple):
    #         msg = email.message_from_bytes(response[1])         #! replace with Python 3.9 methods
    #         if 'message-id' in msg:
    #             msg_ID = msg['message-id']

    for response in msg:
        if isinstance(response, tuple):
            msg = parser.parsebytes(response[1])
            if 'message-id' in msg:
                msg_ID = msg['message-id']

    return res, msg, msg_ID


def parse_PhonePe_email(msg) :
    return


def parse_Sodexo_email(msg) :
    return