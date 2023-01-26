# methods to parse and read the relevant emails

from email.parser import BytesParser
from email.policy import default
from re import sub
from datetime import datetime
from datetime import timedelta
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


def process_PhonePe_email_body_1(text,type,verbose) :
    
    if type == "text/plain" :

        text_no_space = sub(' [ \t]+','\n',text)
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
        
        if verbose :
            print("\nDate : ",datetime_object)
            print("Paid to : ",Paid_to_txt)
            print("Amount : ",currency_char,amount_float)
            print("Transaction message : ",Transaction_msg_txt)

        return dict(type="PhonePe_1", date=datetime_object, paid_to=Paid_to_txt, amount=amount_float, message=Transaction_msg_txt)

    elif type == "text/html" :
        
        soup = BeautifulSoup(text,'html.parser')
        text_str = soup.text

        text_no_space = sub('[\n]+','\n',text_str)
        text_no_space = sub(' [ ]+','\n',text_no_space)
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

        if verbose :
            print("\nDate : ",datetime_object)
            print("Paid to : ",Paid_to_txt)
            print("Amount : ",currency_char,amount_float)
            print("Transaction message : ",Transaction_msg_txt)

        return dict(type="PhonePe_1", date=datetime_object, paid_to=Paid_to_txt, amount=amount_float, message=Transaction_msg_txt)


# def process_PhonePe_email_body_2(text,type) :
        
#     if type == "text/plain" :

#         text_no_space = sub(' [ \t]+','\n',text)
#         #* logic = if two or more spaces come together, it is a long space and is replaced with a newline to split at in the next step 
        
#         lines = text_no_space.splitlines()
#         # print(lines)

#         lines_2 = []
#         for x in lines :
#             if x not in ['','\xa0'] and not x.startswith('<http:'):
#                 lines_2.append(x)
#         print(lines_2)

#         # Date_txt = lines[2]
        
#         # txn_id_index = lines.index('Txn. ID')       # some names come in multiple lines
#         # Amount_txt = lines[txn_id_index-1]
        
#         # Paid_to_txt = " ".join(lines[4:txn_id_index-1])

#         # hi_message_index = lines.index('Hi Gabriel Ve Vance')
#         # if lines[hi_message_index-1] != ':' :
#         #     Transaction_msg_txt = lines[hi_message_index-1]
#         # else :
#         #     Transaction_msg_txt = ''
        
#         # try :
#         #     currency_char = Amount_txt[0]
#         #     amount_float = float(Amount_txt[2:])
#         #     datetime_object = datetime.strptime(Date_txt, '%b %d, %Y')
#         # except :
#         #     currency_char = '$'
#         #     amount_float = 0.0
#         #     datetime_object = datetime.strptime('Jan 1, 2023', '%b %d, %Y')

#         # print("\nDate : ",datetime_object)
#         # print("Paid to : ",Paid_to_txt)
#         # print("Amount : ",currency_char,amount_float)
#         # print("Transaction message : ",Transaction_msg_txt)

#         # return dict(type="PhonePe_1", date=datetime_object, paid_to=Paid_to_txt, amount=amount_float, message=Transaction_msg_txt)
#         return {}

#     elif type == "text/html" :
        
#         soup = BeautifulSoup(text,'html.parser')
#         text_str = soup.text

#         text_no_space = sub('[\n]+','\n',text_str)
#         text_no_space = sub(' [ ]+','\n',text_no_space)
#         lines = text_no_space.splitlines()

#         lines_2 = []
#         for x in lines :
#             if x != ' ' and x != '\xa0' and x != '' :
#                 lines_2.append(x.strip())
#         print(lines_2)

#         # Date_txt = lines_2[1]
        
#         # txn_id_index = lines_2.index('Txn. ID')       # some names come in multiple lines
#         # Amount_txt = lines_2[txn_id_index-1]
        
#         # Paid_to_txt = " ".join(lines_2[3:txn_id_index-1])

#         # hi_message_index = lines_2.index('Hi Gabriel Ve Vance')
#         # if lines_2[hi_message_index-1] != ':' :
#         #     Transaction_msg_txt = lines_2[hi_message_index-1]
#         # else :
#         #     Transaction_msg_txt = ''
        
#         # try :
#         #     currency_char = Amount_txt[0]
#         #     amount_float = float(Amount_txt[2:])
#         #     datetime_object = datetime.strptime(Date_txt, '%b %d, %Y')
#         # except :
#         #     currency_char = '$'
#         #     amount_float = 0.0
#         #     datetime_object = datetime.strptime('Jan 1, 2023', '%b %d, %Y')

#         # print("\nDate : ",datetime_object)
#         # print("Paid to : ",Paid_to_txt)
#         # print("Amount : ",currency_char,amount_float)
#         # print("Transaction message : ",Transaction_msg_txt)

#         # return dict(type="PhonePe_1", date=datetime_object, paid_to=Paid_to_txt, amount=amount_float, message=Transaction_msg_txt)
#         return {}

def parse_PhonePe_email_1(msg,verbose=False) :

    details_dict = {}
    if msg.is_multipart():
        for part in msg.walk():       
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
                body = str(body.decode())
                details_dict = process_PhonePe_email_body_1(body,"text/plain",verbose)
                break

            elif part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                body = str(body.decode())
                details_dict = process_PhonePe_email_body_1(body,"text/html",verbose)
                break
    
    return details_dict
    

def parse_PhonePe_email_2(msg,verbose=False) :
    '''  for this type of PhonePe email, the subject line is what we can use to parse since the body of every type of payment is different. '''

    details_dict = {}

    # amount and paid-to extracted from subject
    subject = msg['Subject']
    part = subject.split('Payment for ')[1]
    part = part.split(' is successful')[0]
    part = (part.split(' of ')[0],part.split(' of ')[1])
    amount_float = float(part[1].split('₹ ')[1])
    
    # date
    date = msg['Date']
    part2 = date.split(' +')[0]
    datetime_object = datetime.strptime(part2, '%a, %d %b %Y %H:%M:%S')
    
    # transaction message is blank
    Transaction_msg_txt = ''

    # print(part)

    # if msg.is_multipart():
    #     for part in msg.walk():       
    #         if part.get_content_type() == "text/plain":
    #             body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
    #             body = str(body.decode())
    #             details_dict = process_PhonePe_email_body_2(body,"text/plain")
    #             break

    #         elif part.get_content_type() == "text/html":
    #             body = part.get_payload(decode=True)
    #             body = str(body.decode())
    #             details_dict = process_PhonePe_email_body_2(body,"text/html")
    #             break

    if verbose :
        print("\nDate : ",datetime_object)
        print("Paid to : ",part[0])
        print("Amount : ",'₹',amount_float)
        print("Transaction message : ",Transaction_msg_txt)

    details_dict = dict(type="PhonePe_2", date=datetime_object, paid_to=part[0], amount=amount_float, message=Transaction_msg_txt)

    return details_dict


def process_Sodexo_email_body(text,email_date,type,verbose) :
    
    if type == "text/plain" :

        text_no_space = sub(' [ \t]+','\n',text)
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

        if verbose :
            print("\nDate : ",datetime_object)
            print("Paid to : ",Paid_to_txt)
            print("Amount : ",currency_char,amount_float)
            print("Transaction message : ",Transaction_msg_txt)

        return dict(type="Sodexo", date=datetime_object, paid_to=Paid_to_txt, amount=amount_float, message=Transaction_msg_txt)

    elif type == "text/html" :
        
        soup = BeautifulSoup(text,'html.parser')
        text_str = soup.text
        # print(text_str)

        text_no_space = sub('[\n]+','\n',text_str)
        text_no_space = sub(' [ ]+','\n',text_no_space)
        lines = text_no_space.splitlines()
        # print(lines)

        lines2 = []
        for x in lines :
            if x not in ['',' ','\xa0'] :
                lines2.append(x.strip())
        # print(lines2)

        # Date_txt = ''       #! write code
        
        TotalAmount_index = lines2.index('Total Amount')
        Amount_txt = lines2[TotalAmount_index+1]

        Paid_to_txt = lines2[2].split('. Please call')[0].split(' at ')[-1]

        # for i in range(len(lines2)) :
        #     if lines2[i].startswith('Receipt ID: ') :
        #         Date_txt = lines2[i+1]
        #         break
        
        try :
            currency_char = Amount_txt[0]
            amount_float = float(Amount_txt[1:])
            # datetime_object = datetime.strptime(Date_txt,'%H:%M,%d %b')
        except :
            currency_char = '$'
            amount_float = 0.0
            # datetime_object = datetime.strptime('Jan 1, 2023', '%b %d, %Y')

        if verbose :
            # print("\nDate1 : ",datetime_object)
            print("\nDate : ",email_date)
            print("Paid to : ",Paid_to_txt)
            print("Amount : ",currency_char,amount_float)
        
        Transaction_msg_txt = ''

        return dict(type="Sodexo", date=email_date, paid_to=Paid_to_txt, amount=amount_float, message=Transaction_msg_txt)


def parse_Sodexo_email(msg,verbose=False) :
    
    # Get email date because email body does not have year information 
    email_date = datetime.strptime(msg['date'].split(' +')[0],'%a, %d %b %Y %H:%M:%S') + timedelta(minutes=30, hours=5)
    
    for part in msg.walk():       
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
            body = str(body.decode())
            details_dict = process_Sodexo_email_body(body,email_date,"text/plain",verbose)
            break

        elif part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            body = str(body.decode())
            details_dict = process_Sodexo_email_body(body,email_date,"text/html",verbose)
            break

    return details_dict    