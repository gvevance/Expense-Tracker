# methods to tabulate transactions
# from datetime import datetime

def process_transaction(details_dict,BUFFER,verbose=False) :
    if verbose :
        print(details_dict)
    BUFFER.append(details_dict)
    return BUFFER


def dump_from_csv_file(CSV_FILE) :
    pass


def dump_to_csv_file(BUFFER,CSV_FILE) :
    
    with open(CSV_FILE,'a+') as csvfile :
        
        for item in BUFFER :
            type = item['type']
            date = item['date'].date()
            paid_to = item['paid_to']
            amount = item['amount']
            message = item['message']

            csvfile.write(f"{type},{date},{paid_to},{amount},{message}\n")
    