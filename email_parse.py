# methods to parse and read the relevant emails

from email.parser import BytesParser
from email.policy import default
import re
from datetime import datetime
from bs4 import BeautifulSoup

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


def process_PhonePe_email_body_1(text,type) :
    
    if type == "text/plain" :

        text_no_space = re.sub(' [ \t]+','\n',text)
        #* logic = if two or more spaces come together, it is a long space and is replaced with a newline to split at in the next step 
        
        lines = text_no_space.splitlines()
        # print(lines)

        Date_txt = lines[2]
        
        txn_id_index = lines.index('Txn. ID')       # some names come in multiple lines
        Amount_txt = lines[txn_id_index-1]
        
        Paid_to_txt = " ".join(lines[4:txn_id_index-1])

        hi_message_index = lines.index('Hi Gabriel Ve Vance')
        if lines[hi_message_index-1] != ':' :
            Transaction_msg_txt = lines[hi_message_index-1]
        else :
            Transaction_msg_txt = ''
        
        try :
            currency_char = Amount_txt[0]
            amount_float = float(Amount_txt[2:])
            datetime_object = datetime.strptime(Date_txt, '%b %d, %Y')
        except :
            currency_char = '$'
            amount_float = 0.0
            datetime_object = datetime.strptime('Jan 1, 2023', '%b %d, %Y')

        print("\nDate : ",datetime_object)
        print("Paid to : ",Paid_to_txt)
        print("Amount : ",currency_char,amount_float)
        print("Transaction message : ",Transaction_msg_txt)

    elif type == "text/html" :
        
        soup = BeautifulSoup(text,'html.parser')
        text_str = soup.text

        text_no_space = re.sub('[\n]+','\n',text_str)
        text_no_space = re.sub(' [ ]+','\n',text_no_space)
        lines = text_no_space.splitlines()

        lines_2 = []
        for x in lines :
            if x != ' ' and x != '\xa0' and x != '' :
                lines_2.append(x.strip())
        # print(lines_2)

        Date_txt = lines_2[1]
        
        txn_id_index = lines_2.index('Txn. ID')       # some names come in multiple lines
        Amount_txt = lines_2[txn_id_index-1]
        
        Paid_to_txt = " ".join(lines_2[3:txn_id_index-1])

        hi_message_index = lines_2.index('Hi Gabriel Ve Vance')
        if lines_2[hi_message_index-1] != ':' :
            Transaction_msg_txt = lines_2[hi_message_index-1]
        else :
            Transaction_msg_txt = ''
        
        try :
            currency_char = Amount_txt[0]
            amount_float = float(Amount_txt[2:])
            datetime_object = datetime.strptime(Date_txt, '%b %d, %Y')
        except :
            currency_char = '$'
            amount_float = 0.0
            datetime_object = datetime.strptime('Jan 1, 2023', '%b %d, %Y')

        print("\nDate : ",datetime_object)
        print("Paid to : ",Paid_to_txt)
        print("Amount : ",currency_char,amount_float)
        print("Transaction message : ",Transaction_msg_txt)



def process_PhonePe_email_body_2(text) :
        
    text_no_space = re.sub(' [ \t]+','\n',text)
    print(text_no_space.splitlines())


def parse_PhonePe_email_1(msg) :

    if msg.is_multipart():
        for part in msg.walk():       
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
                body = str(body.decode())
                process_PhonePe_email_body_1(body,"text/plain")

            elif part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                body = str(body.decode())
                process_PhonePe_email_body_1(body,"text/html")
    

def parse_PhonePe_email_2(msg) :
    return


def parse_Sodexo_email(msg) :
    # body = msg.get_payload(decode=True)
    # body = str(body.decode())
    # process_email_body_whitespaces(body)
    return