# methods to parse and read the relevant emails

from email.parser import BytesParser
from email.policy import default
import re

parser = BytesParser(policy=default)

def get_message_ID(connection,i) :
    res, msg = connection.fetch(str(i), '(RFC822)')
    msg_ID = '0'
    
    for response in msg:
        if isinstance(response, tuple):
            msg = parser.parsebytes(response[1])
            if 'message-id' in msg:
                msg_ID = msg['message-id']

    return res, msg, msg_ID


def process_PhonePe_email_body_1(text) :
    
    # raw_string = unicodedata.normalize('NFC',text)
    # a = []
    # for x in raw_string :
    #     a.append(x)
    # print(a)

    # raw_string = raw_string.replace("  ","")
    # raw_string = raw_string.replace("\t\t","")
    # raw_string = raw_string.replace("\t","")
    
    text_no_space = re.sub(' [ \t]+','\n',text)
    print(text_no_space.splitlines())


def process_PhonePe_email_body_2(text) :
    
    # raw_string = unicodedata.normalize('NFC',text)
    # a = []
    # for x in raw_string :
    #     a.append(x)
    # print(a)

    # raw_string = raw_string.replace("  ","")
    # raw_string = raw_string.replace("\t\t","")
    # raw_string = raw_string.replace("\t","")
    
    text_no_space = re.sub(' [ \t]+','\n',text)
    print(text_no_space.splitlines())


def parse_PhonePe_email_1(msg) :

    if msg.is_multipart():
        for part in msg.walk():       
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
                body = str(body.decode())

    process_PhonePe_email_body_1(body)


def parse_PhonePe_email_2(msg) :
    return


def parse_Sodexo_email(msg) :
    # body = msg.get_payload(decode=True)
    # body = str(body.decode())
    # process_email_body_whitespaces(body)
    return