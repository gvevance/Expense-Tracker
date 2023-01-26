# methods to tabulate transactions
from csv import reader

def process_transaction(details_dict,BUFFER,verbose=False) :
    if verbose :
        print(details_dict)
    BUFFER.append(details_dict)
    return BUFFER

def dump_from_csv_file(CSV_FILE) :
    pass