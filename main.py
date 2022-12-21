from setup import connect_to_server

# return an imap connection object
connection = connect_to_server()

#select INBOX
status,messages = connection.select("\"PhonePe sent or paid\"")
num_of_messages = int(messages[0])
